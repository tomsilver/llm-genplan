"""Utilities."""

import functools
import hashlib
import logging
import os
import subprocess
import urllib.request
from datetime import date
from pathlib import Path
from typing import Any, Dict, List, Set, Tuple
import multiprocessing as mp
import time

from llm_genplan.flags import FLAGS
from llm_genplan.structs import (
    GeneralizedPlan,
    PyperplanObject,
    PyperplanOperator,
    PyperplanPredicate,
    PyperplanType,
    Task,
)

# Global constants.
LLM_QUESTION_TOKEN = "Q:"
LLM_ANSWER_TOKEN = "A:"
_DIR = Path(__file__).parent
PDDL_DIR = _DIR / "envs" / "assets" / "pddl"


@functools.lru_cache(maxsize=None)
def get_git_commit_hash() -> str:
    """Return the hash of the current git commit."""
    out = subprocess.check_output(["git", "rev-parse", "HEAD"])
    return out.decode("ascii").strip()


def get_pddl_from_url(url: str, cache_dir: Path = PDDL_DIR) -> str:
    """Download a PDDL file from a given URL.

    If the file already exists in the cache_dir, load instead.

    Note that this assumes the PDDL won't change at the URL.
    """
    sanitized_url = "".join(x for x in url if x.isalnum())
    file_name = f"cached-pddl-{sanitized_url}"
    file_path = cache_dir / file_name
    # Download if doesn't already exist.
    if not os.path.exists(file_path):
        logging.info(f"Cache not found for {url}, downloading.")
        try:
            with urllib.request.urlopen(url) as f:
                pddl = f.read().decode("utf-8").lower()
        except urllib.error.HTTPError:
            raise ValueError(f"PDDL file not found at {url}.")
        if "(:action" not in pddl and "(:init" not in pddl:
            raise ValueError(f"PDDL file not found at {url}.")
        # Add a note at the top of the file about when this was downloaded.
        today = date.today().strftime("%B %d, %Y")
        note = f"; Downloaded {today} from {url}\n"
        pddl = note + pddl
        # Cache.
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(pddl)
    with open(file_path, "r", encoding="utf-8") as f:
        pddl = f.read()
    return pddl


def pred_to_str(pred: PyperplanPredicate) -> str:
    """Create a string representation of a Pyperplan predicate (atom)."""
    if not pred.signature:
        return f"({pred.name})"
    arg_str = " ".join(str(o) for o, _ in pred.signature)
    return f"({pred.name} {arg_str})"


def get_objects_str(task: Task) -> str:
    """Returns a PDDL encoding of the objects in the task."""
    # Create the objects string.
    type_to_objs: Dict[PyperplanType, List[PyperplanObject]] = {
        t: [] for t in task.domain.types.values()
    }
    for obj in sorted(task.problem.objects):
        obj_type = task.problem.objects[obj]
        type_to_objs[obj_type].append(obj)
    # Construct the object list for the prompt.
    objects_strs: List[str] = []
    for typ, objs in type_to_objs.items():
        if not objs:
            continue
        typ_str = " ".join(objs) + " - " + str(typ)
        objects_strs.append(typ_str)
    return "\n  ".join(objects_strs)


def get_init_strs(task: Task) -> List[str]:
    """Returns the init strings of a PDDL task."""
    init_strs = [pred_to_str(p) for p in task.problem.initial_state]
    return init_strs


def get_init_str(task: Task) -> str:
    """Returns the init string of a PDDL task."""
    init_strs = get_init_strs(task)
    return "\n".join(init_strs)


def get_goal_str(task: Task) -> str:
    """Returns the goal string of a PDDL task."""
    goal_strs = [pred_to_str(p) for p in task.problem.goal]
    goal_str = "\n".join(goal_strs)
    return goal_str


def str_to_identifier(x: str) -> str:
    """Convert a string to a small string with negligible collision probability
    and where the smaller string can be used to identifier the larger string in
    file names.

    Importantly, this function is deterministic between runs and between
    platforms, unlike python's built-in hash function.
    References:
        https://stackoverflow.com/questions/45015180
        https://stackoverflow.com/questions/5297448
    """
    return hashlib.md5(x.encode("utf-8")).hexdigest()


def is_subtype(type1: PyperplanType, type2: PyperplanType) -> bool:
    """Checks whether type1 inherits from type2."""
    while type1 is not None:
        if type1 == type2:
            return True
        type1 = type1.parent
    return False


def reset_flags(args: Dict[str, Any], default_seed: int = 123) -> None:
    """Resets FLAGS for use in unit tests.

    Unless seed is specified, we use a default for testing.
    """
    FLAGS.__dict__.clear()
    FLAGS.__dict__.update(args)
    if "seed" not in FLAGS:
        FLAGS.__dict__["seed"] = default_seed


def action_to_task_operator(task: Task, action: str) -> PyperplanOperator:
    """Look up operator for action and raise ValueError if not found."""
    pyperplan_task = task.pyperplan_task
    for op in pyperplan_task.operators:
        if op.name == action:
            action_op = op
            break
    else:  # pragma: no cover
        raise ValueError(f"Invalid action for task: {action}")
    return action_op


def action_is_valid_for_task(task: Task, action: str) -> bool:
    """Check whether the action is valid in the task initial state."""
    pyperplan_task = task.pyperplan_task
    current_facts = pyperplan_task.initial_state
    action_op = action_to_task_operator(task, action)
    return action_op.applicable(current_facts)


def advance_task(task: Task, action: str) -> Task:
    """Create a new task with a new initial state."""
    action_op = action_to_task_operator(task, action)
    objects_str = get_objects_str(task)
    init_strs = set(get_init_strs(task))
    init_strs = (init_strs - action_op.del_effects) | action_op.add_effects
    init_str = "\n  ".join(sorted(init_strs))
    goal_str = get_goal_str(task)
    new_problem_str = f"""(define (problem synthetic-problem)
   (:domain {task.domain.name})
  (:objects
  {objects_str}
  )
  (:init
  {init_str}
  )
  (:goal
  {goal_str}
  )
)"""
    new_task = Task(task.domain_str, new_problem_str)
    return new_task


def _create_genplan_error_info(task: Task, msg: str) -> str:
    return "\n".join([
        "Given the following inputs:",
        f"objects = {task.objects}",
        f"init = {task.init}",
        f"goal = {task.goal}",
        msg
    ])


def _run_genplan_on_task_no_timeout(
    generalized_plan: GeneralizedPlan, task: Task, horizon: int,
    result_dict: Dict,
) -> None:
    """Helper for run_genplan_on_task()."""
    result_dict["success"] = False
    try:
        plan = generalized_plan.run(task)
    except Exception as e:
        msg = f"The code raised the following exception: {e}"
        result_dict["info"] = _create_genplan_error_info(task, msg)
        return
    if len(plan) > horizon:
        msg = f"The code returned too long of a plan (horizon={horizon})."
        result_dict["info"] = _create_genplan_error_info(task, msg)
        return
    for action in plan:
        if not utils.action_is_valid_for_task(task, action):
            msg = f"The code returned an invalid action: {action}"
            result_dict["info"] = _create_genplan_error_info(task, msg)
            return
        task = advance_task(task, action)
    # Check if goal achieved.
    if task.goal_holds():
        result_dict["success"] = True
        result_dict["info"] = "Generalized plan succeeded."
        return
    msg = ("The code returned the following plan, which did not achieve the "
           f"goal: {plan}")
    result_dict["info"] = _create_genplan_error_info(task, msg)
    return


def run_genplan_on_task(
    generalized_plan: GeneralizedPlan, task: Task, horizon: int, timeout: int,
) -> Tuple[bool, str]:
    """Returns bool success and an info string."""
    # Handle possible timeouts.
    manager = mp.Manager()
    result_dict = manager.dict()
    p = mp.Process(target=_run_genplan_on_task_no_timeout, args=(generalized_plan, task, horizon, result_dict))
    p.start()
    p.join(timeout)
    # Timeout reached.
    if p.is_alive():
        p.kill()
        msg = "The code did not finish in time. Possible infinite loop."
        result_dict["info"] = _create_genplan_error_info(task, msg)
        return False, info
    return result_dict["success"], result_dict["info"]

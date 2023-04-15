"""Utilities."""

import functools
import logging
import multiprocessing as mp
import os
import signal
import subprocess
import sys
import tempfile
import traceback
import urllib.request
from argparse import Namespace
from pathlib import Path
from typing import Dict, List, Set, Tuple

from llm_genplan.flags import FLAGS
from llm_genplan.structs import (
    GeneralizedPlan,
    Task,
)

# Global constants.
_DIR = Path(__file__).parent
PDDL_DIR = _DIR / "envs" / "assets" / "pddl"
CACHE_DIR = _DIR / "llm_cache"


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
        # Cache.
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(pddl)
    with open(file_path, "r", encoding="utf-8") as f:
        pddl = f.read()
    return pddl


def validate_plan(task: Task, plan: List[str]) -> Tuple[bool, str]:
    """Use VAL to check if a plan solves a PDDL problem."""
    plan_str = ""
    for t, action in enumerate(plan):
        plan_str += f"{t}: {action}\n"
    plan_file = tempfile.NamedTemporaryFile(delete=False).name
    with open(plan_file, "w", encoding="utf-8") as f:
        f.write(plan_str)
    val_dir = Path(__file__).parent / "third_party" / "val"
    if sys.platform == "darwin":  # pragma: no cover
        platform_dir = "darwin"
    else:  # pragma: no cover
        assert sys.platform.startswith("linux")
        platform_dir = "linux64"
    val = val_dir / platform_dir / "Validate"
    cmd_str = f'"{val}" -v "{task.domain_file}" "{task.problem_file}" ' f'"{plan_file}"'
    output = subprocess.getoutput(cmd_str)
    os.remove(plan_file)
    if "Plan valid" in output:
        return True, "Plan succeeded."
    repair_phrase = "Plan Repair Advice:"
    if repair_phrase in output:
        msg = output[output.index(repair_phrase) + len(repair_phrase) :]
        msg, _ = msg.split("Failed plans:")
        msg = msg.strip()
    else:
        msg = "The plan did not achieve the goal."
    return False, msg


def _set_to_reproducible_str(s: Set) -> str:
    return "{" + ", ".join(map(repr, sorted(s))) + "}"


def _create_genplan_error_info(task: Task, msg: str, flags: Namespace) -> str:
    if not flags.include_inputs_in_feedback:
        return msg
    sorted_obj_str = _set_to_reproducible_str(task.objects)
    sorted_init_str = _set_to_reproducible_str(task.init)
    sorted_goal_str = _set_to_reproducible_str(task.goal)
    return "\n".join(
        [
            "Given the following inputs:",
            f"objects = {sorted_obj_str}",
            f"init = {sorted_init_str}",
            f"goal = {sorted_goal_str}",
            msg,
        ]
    )


def _run_genplan_on_task_no_timeout(
    generalized_plan: GeneralizedPlan,
    task: Task,
    horizon: int,
    result_dict: Dict,
    flags: Namespace,
) -> None:
    """Helper for run_genplan_on_task()."""
    result_dict["success"] = False
    try:
        plan = generalized_plan.run(task)
    except BaseException as e:  # pylint: disable=broad-exception-caught
        tb = traceback.format_exception(e)
        tb_lines = [
            l.replace(str(generalized_plan.filepath), "<file-name-omitted>")
            for l in tb
            if "llm_genplan" not in l
        ]
        tb_str = "".join(tb_lines)
        msg = f"The code raised the following exception:\n{tb_str}"
        result_dict["info"] = _create_genplan_error_info(task, msg, flags)
        return
    if not isinstance(plan, list):
        msg = f"The code returned {plan}, which is not a list of actions."  # type: ignore[unreachable] # pylint:disable=line-too-long
        result_dict["info"] = _create_genplan_error_info(task, msg, flags)
        return
    if len(plan) > horizon:
        msg = f"The code returned too long of a plan (horizon={horizon})."
        result_dict["info"] = _create_genplan_error_info(task, msg, flags)
        return

    # Check syntax.
    for t, action in enumerate(plan):
        if not task.action_has_valid_syntax(action):
            msg = (
                f"The code returned this plan: {plan}\n"
                f"However, the action {action} is invalid at step {t}.\n"
                f"NOTE: the valid operators are: {task.actions_hint}."
            )
            result_dict["info"] = _create_genplan_error_info(task, msg, flags)
            return

    # Check semantics.
    plan_is_valid, info = validate_plan(task, plan)
    if plan_is_valid:
        result_dict["success"] = True
        result_dict["info"] = "Generalized plan succeeded."
        return
    msg = f"The code failed. It returned the following plan: {plan}.\n{info}"
    result_dict["info"] = _create_genplan_error_info(task, msg, flags)
    return


def run_genplan_on_task(
    gen_plan: GeneralizedPlan,
    task: Task,
    horizon: int,
    timeout: int,
) -> Tuple[bool, str]:
    """Returns bool success and an info string."""

    # Uncomment for debugging.
    # result_dict = {}
    # _run_genplan_on_task_no_timeout(gen_plan, task, horizon, result_dict, FLAGS)

    # Handle possible timeouts.
    manager = mp.Manager()
    result_dict = manager.dict()
    p = mp.Process(
        target=_run_genplan_on_task_no_timeout,
        args=(gen_plan, task, horizon, result_dict, FLAGS),
    )
    p.start()
    p.join(timeout)
    # Timeout reached.
    if p.is_alive():
        # Treated like a KeyboardInterrupt.
        assert p.pid is not None
        os.kill(p.pid, signal.SIGINT)
        # Give it a few more seconds then kill for good.
        p.join(3)
        p.kill()
        # Add a little more info.
        result_dict["info"] = result_dict.get("info", "") + (
            "\nThe code was interrupted because it timed out "
            "(possible infinite loop)."
        )

    return result_dict["success"], result_dict["info"]

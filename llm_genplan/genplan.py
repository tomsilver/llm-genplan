"""Interact with an LLM to get a generalized plan."""

import importlib.util
import logging
import multiprocessing as mp
import os
import signal
import sys
import tempfile
import time
import traceback
from argparse import Namespace
from dataclasses import dataclass
from functools import cached_property
from pathlib import Path
from typing import Dict, List, Optional, Tuple

import pyperclip
from numpy import NaN

from llm_genplan import utils
from llm_genplan.envs import get_prompt_problem_distribution
from llm_genplan.flags import FLAGS
from llm_genplan.structs import Metrics, Task

GENPLAN_ERROR_TYPES = [
    "timeout",
    "python-exception",
    "output-not-plan",
    "operator-syntax-invalid",
    "operator-semantics-invalid",
]


@dataclass(frozen=True)
class GeneralizedPlan:
    """Wrapper around a generalized plan code string."""

    code_str: str

    @cached_property
    def filepath(self) -> Path:
        """Get a file with the code string implemented in it."""
        filename = Path(tempfile.NamedTemporaryFile(delete=False, suffix=".py").name)
        with open(filename, "w", encoding="utf-8") as f:
            f.write(self.code_str)
        return filename

    def run(self, task: Task) -> List[str]:
        """Run the generalized plan to get a plan for the task."""
        # Import get_plan().
        module_name = f"{self.filepath.stem}"
        spec = importlib.util.spec_from_file_location(module_name, self.filepath)
        assert spec is not None
        assert spec.loader is not None
        module = importlib.util.module_from_spec(spec)
        assert module is not None
        sys.modules[module_name] = module
        spec.loader.exec_module(module)
        # Run the generalized plan.
        return module.get_plan(task.objects, task.init, task.goal)  # type: ignore  # pylint: disable=undefined-variable


def get_genplan_from_llm(
    prompt_tasks: List[Task],
    extra_train_tasks: List[Task],
    save_path: Path,
    horizon: int,
    timeout: int,
    max_debug_attempts: int = 4,
) -> Tuple[GeneralizedPlan, Metrics]:
    """Interact with an LLM to get a generalized plan."""
    metrics: Metrics = {}

    # Initial prompt with domain and example problems.
    all_train_tasks = prompt_tasks + extra_train_tasks
    domain_str = all_train_tasks[0].domain_str
    assert all(t.domain_str == domain_str for t in all_train_tasks)
    problem_strs: List[str] = []
    for task in prompt_tasks:
        if FLAGS.abbreviate_problem_strs:
            problem_str = task.get_abbreviated_problem_str()
        else:
            problem_str = task.problem_str
        problem_strs.append(problem_str)
    problems_str = "\n".join(problem_strs)
    prompt0 = f"Domain:\n{domain_str.strip()}\n\n"
    if problems_str:
        prompt0 += f"Example problems:\n{problems_str.strip()}\n"

    if not FLAGS.skip_chain_of_thought:
        prompt0 += "Write a short summary of this domain in words."
        run_prompt(prompt0, save_path, prompt_num=0)

        # Optionally show some representation of the problem distribution, like
        # (partial) code that generates problems.
        if FLAGS.prompt_problem_distribution != "none":
            dist_str = get_prompt_problem_distribution(
                FLAGS.env, FLAGS.prompt_problem_distribution
            )
            prompt1 = f"Problem distribution:\n{dist_str.strip()}\n\n"
            prompt1 += "Write a short summary of the problem distribution in words."
            run_prompt(prompt1, save_path, prompt_num=1)

        # Simple strategy without search.
        prompt2 = (
            "There is a simple strategy for solving all problems in this domain "
            "without using search. What is that strategy?"
        )
        run_prompt(prompt2, save_path, prompt_num=2)

    # Python function.
    if all_train_tasks[0].typed:
        objects_description = "a set of (object name, type name) tuples"
    else:
        objects_description = "a set of objects (string names)"

    first_genplan_prompt = f"""Implement the strategy as a Python function.

The code should should be of the form

def get_plan(objects, init, goal):
    # Your code here
    return plan

where
    - `objects` is {objects_description}
    - `init` is a set of ground atoms represented as tuples of predicate
       names and arguments (e.g., ('predicate-foo', 'object-bar', ...))
    - `goal` is also a set of ground atoms represented in the same way
    - `plan` is a list of actions, where each action is a ground operator
       represented as a string (e.g., '(operator-baz object-qux ...)')
"""

    if FLAGS.skip_chain_of_thought:
        no_cot_prompt0 = prompt0
        no_cot_prompt0 += (
            "There is a simple strategy for solving all problems in this "
            "domain without using search. "
        )
        no_cot_prompt0 += first_genplan_prompt
        first_genplan_prompt = no_cot_prompt0

    last_error_info: Optional[str] = None
    gen_plan_code_str = ""
    metrics["num_interactive_debugs"] = 0
    metrics["num_influential_training_tasks"] = len(prompt_tasks)
    for err in GENPLAN_ERROR_TYPES:
        metrics[err] = 0

    for t in range(max_debug_attempts + 1):
        # Get the prompt.
        if t == 0:
            prompt = first_genplan_prompt
        else:
            assert last_error_info is not None
            prompt = f"{last_error_info}\nFix the code."
            metrics["num_interactive_debugs"] += 1

        # Query.
        response = run_prompt(prompt, save_path, prompt_num=3 + t)
        if response is None:
            break

        # Note: appending the response so that if the LLM is relying on any
        # helper functions that it previously defined, they will be available.
        # If it rewrites `get_plan`, the newer code will take precedence.
        # However, only keep the response for the next iteration if there is
        # no parsing error because otherwise it would be impossible to correct.
        new_gen_plan_code_str = gen_plan_code_str + "\n\n\n" + response
        gen_plan = GeneralizedPlan(new_gen_plan_code_str)

        # Test the generalized plan.
        gen_plan_succeeded = True
        parsing_error_found = False
        for i, task in enumerate(all_train_tasks):
            success, info, task_metrics = run_genplan_on_task(
                gen_plan, task, horizon, timeout
            )
            for err in GENPLAN_ERROR_TYPES:
                metrics[err] += task_metrics[err]
            if "SyntaxError" in info:
                parsing_error_found = True
            if not success:
                gen_plan_succeeded = False
                last_error_info = info
                metrics["num_influential_training_tasks"] = max(
                    metrics["num_influential_training_tasks"],
                    i + 1,
                )
                break

        # See note above about parsing errors.
        if not parsing_error_found:
            gen_plan_code_str = new_gen_plan_code_str

        # Succeeded on the training problems.
        if gen_plan_succeeded:
            break

    return GeneralizedPlan(gen_plan_code_str), metrics


def run_prompt(prompt: str, save_path: Path, prompt_num: int) -> Optional[str]:
    """For now, query the LLM by hand."""
    # Set up save and load paths.
    prompt_path = save_path / f"{prompt_num}-prompt.txt"
    response_path = save_path / f"{prompt_num}-response.txt"
    if prompt_path.exists():
        # If already exists, assert that the prompt is unchanged.
        with open(prompt_path, "r", encoding="utf-8") as f:
            saved_prompt = f.read()
        if saved_prompt != prompt:
            logging.warning("Saved prompt:")
            logging.warning(saved_prompt)
            logging.warning("New prompt:")
            logging.warning(prompt)
            # Special case timeouts because they can be nondeterministic.
            if "KeyboardInterrupt" in prompt:
                assert "KeyboardInterrupt" in saved_prompt
            elif FLAGS.force_load_from_cache:
                logging.warning("WARNING: Forced loading saved prompt from cache.")
            else:
                raise RuntimeError("Loading failed.")
        # Load the saved response.
        with open(response_path, "r", encoding="utf-8") as f:
            saved_response = f.read()
        logging.info(f"Loaded response from {response_path}.")
        return _parse_python_code_from_response(saved_response)
    # Do new prompt.
    logging.info("Prompt:")
    logging.info(prompt)
    pyperclip.copy(prompt)
    logging.info("The prompt is now copied to your clipboard.")
    user_input = input("Press enter after copying the response or (q) to quit ")
    if "q" in user_input:
        return None
    response = str(pyperclip.paste())
    logging.info("Received response:")
    logging.info(response)
    # Save prompt and response.
    with open(prompt_path, "w", encoding="utf-8") as f:
        f.write(prompt)
    with open(response_path, "w", encoding="utf-8") as f:
        f.write(response)
    logging.info(f"Saved response to {response_path}.")
    return _parse_python_code_from_response(response)


def _parse_python_code_from_response(response: str) -> str:
    # Parse out python code if it exists.
    python_code_prefix = "```python"
    if python_code_prefix in response:
        python_start = response.index(python_code_prefix)
        python_remainder = response[python_start + len(python_code_prefix) :]
        if "```" in python_remainder:
            python_end = python_remainder.index("```")
        else:
            python_end = len(python_remainder)
        python_response = python_remainder[:python_end]
        return python_response
    return response


def _create_genplan_error_info(task: Task, msg: str, flags: Namespace) -> str:
    if flags.exclude_inputs_in_feedback:
        return msg
    if flags.abbreviate_problem_strs:
        problem_str = task.get_abbreviated_problem_str()
    else:
        problem_str = task.problem_str
    return f"Given this task:\n{problem_str}\n{msg}"


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
        result_dict["error-type"] = "python-exception"
        return
    if not isinstance(plan, list):
        msg = f"The code returned {plan}, which is not a list of actions."  # type: ignore[unreachable] # pylint:disable=line-too-long
        result_dict["info"] = _create_genplan_error_info(task, msg, flags)
        result_dict["error-type"] = "output-not-plan"
        return
    assert len(plan) <= horizon, "Horizon not currently used."
    result_dict["plan-length"] = len(plan)

    # Check syntax.
    for t, action in enumerate(plan):
        if not task.action_has_valid_syntax(action):
            msg = (
                f"The code returned this plan: {plan}\n"
                f"However, the action {action} is invalid at step {t}.\n"
                f"NOTE: the valid operators are: {task.actions_hint}."
            )
            result_dict["info"] = _create_genplan_error_info(task, msg, flags)
            result_dict["error-type"] = "operator-syntax-invalid"
            return

    # Check semantics.
    plan_is_valid, info = utils.validate_plan(task, plan)
    if plan_is_valid:
        result_dict["success"] = True
        result_dict["info"] = "Generalized plan succeeded."
        return
    msg = f"The code failed. It returned the following plan: {plan}.\n{info}"
    result_dict["info"] = _create_genplan_error_info(task, msg, flags)
    result_dict["error-type"] = "operator-semantics-invalid"
    return


def run_genplan_on_task(
    gen_plan: GeneralizedPlan,
    task: Task,
    horizon: int,
    timeout: Optional[int],
) -> Tuple[bool, str, Metrics]:
    """Returns bool success and an info string."""

    timed_out = False
    start_time = time.perf_counter()

    # For debugging and tests.
    if timeout is None:
        result_dict: Dict = {}
        _run_genplan_on_task_no_timeout(gen_plan, task, horizon, result_dict, FLAGS)

    # Handle possible timeouts.
    else:
        manager = mp.Manager()
        result_proxy_dict = manager.dict()
        p = mp.Process(
            target=_run_genplan_on_task_no_timeout,
            args=(gen_plan, task, horizon, result_proxy_dict, FLAGS),
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
            result_proxy_dict["success"] = False
            result_proxy_dict["info"] = result_proxy_dict.get("info", "") + (
                "\nThe code was interrupted because it timed out "
                "(possible infinite loop)."
            )
            timed_out = True
        result_dict = dict(result_proxy_dict)

    duration = time.perf_counter() - start_time
    task_metrics: Metrics = {err: 0 for err in GENPLAN_ERROR_TYPES}
    task_metrics["duration"] = duration
    task_metrics["plan-length"] = result_dict.get("plan-length", NaN)
    if timed_out:
        assert timeout is not None
        assert duration > timeout
        task_metrics["timeout"] = 1
    if "error-type" in result_dict:
        task_metrics[result_dict["error-type"]] = 1

    return result_dict["success"], result_dict["info"], task_metrics

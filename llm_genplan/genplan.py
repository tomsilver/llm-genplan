"""Interact with an LLM to get a generalized plan."""

import logging
from pathlib import Path
from typing import List, Optional

import pyperclip

from llm_genplan import utils
from llm_genplan.structs import GeneralizedPlan, Task


def get_genplan_from_llm(
    prompt_tasks: List[Task],
    extra_train_tasks: List[Task],
    save_path: Path,
    horizon: int,
    timeout: int,
    max_debug_attempts: int = 8,
) -> GeneralizedPlan:
    """Interact with an LLM to get a generalized plan."""
    # Initial prompt with domain and example problems.
    all_train_tasks = prompt_tasks + extra_train_tasks
    domain_str = all_train_tasks[0].domain_str
    assert all(t.domain_str == domain_str for t in all_train_tasks)
    problems_str = "\n".join([t.problem_str for t in prompt_tasks])
    prompt0 = (
        f"Domain:\n{domain_str.strip()}\n\n"
        f"Example problems:\n{problems_str.strip()}\n"
        "Write a short summary of this domain in words."
    )
    run_prompt(prompt0, save_path, prompt_num=0)

    # Simple strategy without search.
    prompt1 = (
        "There is a simple strategy for solving all problems in this domain "
        "without using search. What is that strategy?"
    )
    run_prompt(prompt1, save_path, prompt_num=1)

    # Python function.
    if all_train_tasks[0].typed:
        objects_description = "a set of (object name, type name) tuples"
    else:
        objects_description = "a set of objects (string names)"
    first_genplan_prompt = f"""Implement the strategy as a Python function.

The code should should be of the form

    # Optional helper functions
    from llm_genplan.utils import get_next_state

    def get_plan(task):
        # Your code here
        return plan

where
    - `task.objects` is {objects_description}
    - `task.init` is a set of ground atoms represented as tuples of predicate
       names and arguments (e.g., ('predicate-foo', 'object-bar', ...))
    - `task.goal` is also a set of ground atoms represented in the same way
    - `plan` is a list of actions, where each action is a ground operator
       represented as a string (e.g., '(operator-baz object-qux ...)')
    - `get_next_state(task, atoms, action)` applies the PDDL operator for `action`
       to `atoms` and returns the next state (set of ground atoms)"""

    last_error_info: Optional[str] = None
    gen_plan_code_str = ""

    for t in range(max_debug_attempts):
        # Get the prompt.
        if t == 0:
            prompt = first_genplan_prompt
        else:
            assert last_error_info is not None
            prompt = f"{last_error_info}\nFix the code."

        # Query.
        response = run_prompt(prompt, save_path, prompt_num=2 + t)
        if response is None:
            break

        # Note: appending the response so that if the LLM is relying on any
        # helper functions that it previously defined, they will be available.
        # If it rewrites `get_plan`, the newer code will take precedence.
        gen_plan_code_str += "\n\n\n" + response
        gen_plan = GeneralizedPlan(gen_plan_code_str)

        # Test the generalized plan.
        gen_plan_succeeded = True
        for task in all_train_tasks:
            success, info = utils.run_genplan_on_task(gen_plan, task, horizon, timeout)
            if not success:
                gen_plan_succeeded = False
                last_error_info = info
                break

        # Succeeded on the training problem.
        if gen_plan_succeeded:
            break

    return GeneralizedPlan(gen_plan_code_str)


def run_prompt(prompt: str, save_path: Path, prompt_num: int) -> Optional[str]:
    """For now, query the LLM by hand."""
    # Set up save and load paths.
    prompt_path = save_path / f"{prompt_num}-prompt.txt"
    response_path = save_path / f"{prompt_num}-response.txt"
    if prompt_path.exists():
        # If already exists, assert that the prompt is unchanged.
        with open(prompt_path, "r", encoding="utf-8") as f:
            saved_prompt = f.read()
        assert saved_prompt == prompt
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
        python_end = python_remainder.index("```")
        python_response = python_remainder[:python_end]
        return python_response
    return response

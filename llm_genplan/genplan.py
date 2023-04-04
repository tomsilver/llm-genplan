"""Interact with an LLM to get a generalized plan."""

import logging
from pathlib import Path
from typing import List, Optional

import pyperclip

from llm_genplan import utils
from llm_genplan.structs import GeneralizedPlan, Task


def get_genplan_from_llm(
    train_tasks: List[Task],
    save_path: Path,
    horizon: int,
    timeout: int,
    max_debug_attempts: int = 8,
) -> GeneralizedPlan:
    """Interact with an LLM to get a generalized plan."""
    # Initial prompt with domain and example problems.
    domain_str = train_tasks[0].domain_str
    assert all(t.domain_str == domain_str for t in train_tasks)
    problems_str = "\n".join([t.problem_str for t in train_tasks])
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
    if train_tasks[0].typed:
        objects_description = "`objects` is a set of (object name, type name) tuples"
    else:
        objects_description = "`objects` is a set of objects (string names)"
    first_genplan_prompt = f"""Implement the strategy as a Python function.

The code should should be of the form

    def get_plan(objects, init, goal):
        # Your code here
        return plan

where
    - {objects_description}
    - `init` is a set of ground atoms represented as tuples of predicate
        names and arguments (e.g., ('predicate-foo', 'object-bar', ...))
    - `goal` is also a set of ground atoms represented in the same way
    - `plan` is a list of actions, where each action is represented as a
        tuple of operator name and arguments (e.g., ('operator-baz',
        'object-qux', ...))."""

    last_error_info: Optional[str] = None

    for t in range(max_debug_attempts):
        # Get the prompt.
        if t == 0:
            prompt = first_genplan_prompt
        else:
            assert last_error_info is not None
            prompt = f"{last_error_info}\nFix the code."

        # Query.
        gen_plan_code_str = run_prompt(prompt, save_path, prompt_num=2 + t)
        gen_plan = GeneralizedPlan(gen_plan_code_str)

        # Test the generalized plan.
        gen_plan_succeeded = True
        for task in train_tasks:
            success, info = utils.run_genplan_on_task(gen_plan, task, horizon, timeout)
            if not success:
                gen_plan_succeeded = False
                last_error_info = info
                break

        # Succeeded on the training problem.
        if gen_plan_succeeded:
            break

    return GeneralizedPlan(gen_plan_code_str)


def run_prompt(prompt: str, save_path: Path, prompt_num: int) -> str:
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
        return saved_response
    # Do new prompt.
    logging.info("Prompt:")
    logging.info(prompt)
    pyperclip.copy(prompt)
    logging.info("The prompt is now copied to your clipboard.")
    input("Press enter after copying the response.")
    response = str(pyperclip.paste())
    logging.info("Received response:")
    logging.info(response)
    # Save prompt and response.
    with open(prompt_path, "w", encoding="utf-8") as f:
        f.write(prompt)
    with open(response_path, "w", encoding="utf-8") as f:
        f.write(response)
    logging.info(f"Saved response to {response_path}.")
    return response

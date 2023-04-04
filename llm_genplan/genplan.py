"""Interact with an LLM to get a generalized plan."""

import logging
from typing import List, Optional

import pyperclip

from llm_genplan import utils
from llm_genplan.structs import GeneralizedPlan, Task


def get_genplan_from_llm(
    train_tasks: List[Task], horizon: int, timeout: int, max_debug_attempts: int = 8
) -> GeneralizedPlan:
    """Interact with an LLM to get a generalized plan."""
    # Initial prompt with domain and example problems.
    domain_str = train_tasks[0].domain_str
    assert all(t.domain_str == domain_str for t in train_tasks)
    problems_str = "\n".join([t.problem_str for t in train_tasks])
    prompt0 = (
        f"Domain:\n{domain_str.strip()}\n\n"
        f"Example problems:\n{problems_str.strip()}"
    )
    run_prompt(prompt0)

    # Summarize the domain.
    prompt1 = "Write a short summary of this domain in words."
    run_prompt(prompt1)

    # Simple strategy without search.
    prompt2 = (
        "There is a simple strategy for solving all problems in this domain "
        "without using search. What is that strategy?"
    )
    run_prompt(prompt2)

    # Python function.
    first_genplan_prompt = """Implement the strategy as a Python function.

The code should should be of the form

    def get_plan(objects, init, goal):
        # Your code here
        return plan

where
    - `objects` is a set of (object name, object type name) tuples
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
        gen_plan_code_str = run_prompt(prompt)
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

        # Requery to debug.
        assert last_error_info is not None
        debug_prompt = f"{last_error_info}\nFix the code."
        gen_plan_code_str = run_prompt(debug_prompt)

    return GeneralizedPlan(gen_plan_code_str)


def run_prompt(prompt: str) -> str:
    """For now, query the LLM by hand."""
    logging.info("Prompt:")
    logging.info(prompt)
    pyperclip.copy(prompt)
    logging.info("The prompt is now copied to your clipboard.")
    input("Press enter after copying the response.")
    response = str(pyperclip.paste())
    logging.info("Received response:")
    logging.info(response)
    return response

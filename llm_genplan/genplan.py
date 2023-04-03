"""Interact with an LLM to get a generalized plan."""

from typing import List

from llm_genplan.structs import GeneralizedPlan, Task


def get_genplan_from_llm(train_tasks: List[Task]) -> GeneralizedPlan:
    """Interact with an LLM to get a generalized plan."""
    # Coming soon
    del train_tasks
    gen_plan_code_str = """def get_plan(objects, init, goal):
    return []
"""
    return GeneralizedPlan(gen_plan_code_str)

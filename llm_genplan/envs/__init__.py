"""Create PDDL training and evaluation tasks."""

from typing import List, Tuple

import pddlgym

from llm_genplan import utils
from llm_genplan.structs import Task


def create_tasks(
    env_name: str,
    num_train: int,
    num_eval: int,
) -> Tuple[List[Task], List[Task]]:
    """Create PDDL training and evaluation tasks."""
    total_num_tasks = num_train + num_eval

    if env_name.startswith("pyperplan-"):
        benchmark_name = env_name[len("pyperplan-") :]
        tasks = _get_pyperplan_tasks(benchmark_name, total_num_tasks)

    elif env_name.startswith("pddlgym-"):
        benchmark_name = env_name[len("pddlgym-") :]
        tasks = _get_pddlgym_tasks(benchmark_name, num_train)
        tasks += _get_pddlgym_tasks(benchmark_name, num_eval, test=True)
    else:
        raise NotImplementedError(f"Unrecognized env: {env_name}.")

    # Sort from smallest to largest.
    sorted_tasks = sorted(tasks, key=lambda t: t.size)
    # Use shortest for training.
    train_tasks = sorted_tasks[:num_train]
    eval_tasks = sorted_tasks[num_train:]
    assert len(eval_tasks) == num_eval

    return train_tasks, eval_tasks


def _get_pyperplan_tasks(benchmark_name: str, num_tasks: int) -> List[Task]:
    """Get PDDL tasks from the pyperplan benchmark set."""
    url_prefix = (
        "https://raw.githubusercontent.com/aibasel/pyperplan/main/"
        f"benchmarks/{benchmark_name}"
    )
    # Download the domain.
    domain_url = url_prefix + "/" + "domain.pddl"
    domain_str = utils.get_pddl_from_url(domain_url)
    # Download the problems.
    tasks = []
    for task_num in range(1, num_tasks + 1):
        problem_url = url_prefix + "/" + f"task{task_num:02d}.pddl"
        try:
            problem_str = utils.get_pddl_from_url(problem_url)
        except ValueError as e:
            assert "PDDL file not found" in str(e)
            raise ValueError(f"Could not download {problem_url}. " "Too many tasks?")
        task = Task(domain_str, problem_str)
        tasks.append(task)
    return tasks


def _get_pddlgym_tasks(
    benchmark_name: str, num_tasks: int, test: bool = False
) -> List[Task]:
    """Get PDDL tasks from PDDLGym."""
    if test:
        test_suffix = "Test"
    else:
        test_suffix = ""
    env_name = f"PDDLEnv{benchmark_name.capitalize()}{test_suffix}-v0"
    env = pddlgym.make(env_name).unwrapped
    # Access the domain.
    domain_str = env.domain.domain
    # Access the problems.
    tasks = []
    for i in range(num_tasks):
        try:
            problem = env.problems[i]
            problem_str = problem.problem
        except IndexError:
            raise ValueError(f"Could not find PDDLGym problem {i}. " "Too many tasks?")
        task = Task(domain_str, problem_str)
        tasks.append(task)
    return tasks

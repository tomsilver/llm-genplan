"""Create PDDL prompting, training, and evaluation tasks."""

from typing import List, Tuple

import pddlgym

from llm_genplan import utils
from llm_genplan.flags import FLAGS
from llm_genplan.structs import Task


def create_tasks(
    env_name: str,
    num_prompt: int,
    num_train: int,
    num_eval: int,
) -> Tuple[List[Task], List[Task], List[Task]]:
    """Create PDDL prompting, training, and evaluation tasks."""
    total_num_tasks = num_prompt + num_train + num_eval

    if env_name.startswith("pyperplan-"):
        benchmark_name = env_name[len("pyperplan-") :]
        tasks = _get_pyperplan_tasks(benchmark_name, total_num_tasks)

    elif env_name.startswith("pddlgym-"):
        benchmark_name = env_name[len("pddlgym-") :]
        tasks = _get_pddlgym_tasks(benchmark_name, num_prompt + num_train)
        tasks += _get_pddlgym_tasks(benchmark_name, num_eval, test=True)

    elif env_name.startswith("custom-"):
        benchmark_name = env_name[len("custom-") :]
        tasks = _get_custom_tasks(benchmark_name, total_num_tasks)

    elif env_name.startswith("pg3-"):
        benchmark_name = env_name[len("pg3-") :]
        return _get_pg3_tasks(benchmark_name, num_prompt, num_train, num_eval)

    else:
        raise NotImplementedError(f"Unrecognized env: {env_name}.")

    # Sort from smallest to largest.
    sorted_tasks = sorted(tasks, key=lambda t: t.size)
    # Use shortest for prompting, next shortest for training.
    prompt_tasks = sorted_tasks[:num_prompt]
    train_tasks = sorted_tasks[num_prompt : (num_prompt + num_train)]
    eval_tasks = sorted_tasks[(num_prompt + num_train) :]
    assert len(eval_tasks) == num_eval

    return prompt_tasks, train_tasks, eval_tasks


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
    domain_str = env.domain.domain.lower()
    # Access the problems.
    tasks = []
    for i in range(num_tasks):
        try:
            problem = env.problems[i]
            problem_str = problem.problem.lower()
        except IndexError:
            raise ValueError(f"Could not find PDDLGym problem {i}. " "Too many tasks?")
        task = Task(domain_str, problem_str)
        tasks.append(task)
    return tasks


def _get_custom_tasks(benchmark_name: str, num_tasks: int) -> List[Task]:
    """Get tasks saved locally."""
    benchmark_dir = utils.PDDL_DIR / "custom" / benchmark_name
    domain_file_path = benchmark_dir / "domain.pddl"
    assert domain_file_path.exists(), f"Domain not found: {domain_file_path}"
    # Load the domain.
    with open(domain_file_path, "r", encoding="utf-8") as f:
        domain_str = f.read().lower()
    # Load the problems.
    all_tasks: List[Task] = []
    for file_path in benchmark_dir.glob("*.pddl"):
        if file_path.stem == "domain.pddl":
            continue
        with open(file_path, "r", encoding="utf-8") as f:
            problem_str = f.read().lower()
        task = Task(domain_str, problem_str)
        all_tasks.append(task)
    # Make sure we have enough problems.
    assert len(all_tasks) >= num_tasks
    return all_tasks


def _get_pg3_tasks(
    benchmark_name: str, num_prompt: int, num_train: int, num_eval: int
) -> Tuple[List[Task], List[Task], List[Task]]:
    """Get PDDL tasks that are stored locally, taken from the PG3 paper."""
    pg3_pddl_dir = utils.PDDL_DIR / "pg3"
    domain_file_path = pg3_pddl_dir / f"{benchmark_name}.pddl"
    assert domain_file_path.exists(), f"Domain not found: {domain_file_path}"
    train_dir = pg3_pddl_dir / benchmark_name / f"seed{FLAGS.seed}"
    assert train_dir.exists(), f"Train dir not found: {train_dir}"
    test_dir = pg3_pddl_dir / f"{benchmark_name}_test" / f"seed{FLAGS.seed}"
    assert test_dir.exists(), f"Test dir not found: {test_dir}"
    # Load the domain.
    with open(domain_file_path, "r", encoding="utf-8") as f:
        domain_str = f.read().lower()
    # Load the train problems.
    all_train_tasks: List[Task] = []
    for train_file_path in train_dir.glob("*.pddl"):
        with open(train_file_path, "r", encoding="utf-8") as f:
            problem_str = f.read().lower()
        task = Task(domain_str, problem_str)
        all_train_tasks.append(task)
    # Make sure we have enough train problems.
    assert len(all_train_tasks) >= num_prompt + num_train
    # Partition into prompt and train.
    prompt_tasks = all_train_tasks[:num_prompt]
    train_tasks = all_train_tasks[num_prompt : (num_prompt + num_train)]
    # Load the test problems.
    all_test_tasks: List[Task] = []
    for test_file_path in test_dir.glob("*.pddl"):
        with open(test_file_path, "r", encoding="utf-8") as f:
            problem_str = f.read().lower()
        task = Task(domain_str, problem_str)
        all_test_tasks.append(task)
    # Make sure we have enough eval problems.
    assert len(all_test_tasks) >= num_eval
    eval_tasks = all_test_tasks[:num_eval]
    return prompt_tasks, train_tasks, eval_tasks


def get_prompt_problem_distribution(env_name: str, dist_type: str) -> str:
    """Get a representation of the problem distribution for this env."""
    filepath = utils.PDDL_DIR / "prompt_problem_dists" / dist_type / f"{env_name}.txt"
    with open(filepath, "r", encoding="utf-8") as f:
        dist_str = f.read()
    return dist_str

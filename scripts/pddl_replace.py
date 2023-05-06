"""Create PDDL domains and problems with all names ablated."""

import os
import re
from typing import Dict

from llm_genplan import utils
from llm_genplan.envs import create_tasks
from llm_genplan.flags import FLAGS, parse_flags
from llm_genplan.structs import Task


def _main() -> None:
    parse_flags()
    prompt_tasks, extra_train_tasks, eval_tasks = create_tasks(
        env_name=FLAGS.env,
        num_prompt=FLAGS.num_prompt_tasks,
        num_train=FLAGS.num_extra_train_tasks,
        num_eval=FLAGS.num_eval_tasks,
    )
    all_tasks = prompt_tasks + extra_train_tasks + eval_tasks
    assert FLAGS.env.startswith("pg3-")
    env = FLAGS.env[len("pg-3") :]
    new_domain_file = utils.PDDL_DIR / "pg3" / f"{env}-ablated.pddl"
    # Get substitutions for domain.
    substitutions = _get_domain_substitutions(all_tasks[0])
    # Apply the substitutions to get a new domain.
    original_domain_str = all_tasks[0].domain_str
    new_domain_str = _apply_substitutions(original_domain_str, substitutions)
    with open(new_domain_file, "w", encoding="utf-8") as f:
        f.write(new_domain_str)
    print(f"Wrote out to {new_domain_file}")
    # Get substitutions for each task.
    for i, task in enumerate(all_tasks):
        task_substitutions = _get_task_substitutions(task, substitutions, i)
        # Apply the substitutions to get a new problem.
        new_problem_str = _apply_substitutions(task.problem_str, task_substitutions)
        # Validate the problem by making sure that the plan length hasn't changed.
        # Only do this for the train tasks for efficiency.
        is_test_task = i >= len(prompt_tasks) + len(extra_train_tasks)
        if not is_test_task:
            new_task = Task(new_domain_str, new_problem_str)
            _validate_transformed_task(new_task, task)
        # Save the new task.
        if is_test_task:
            new_dir_name = f"{env}-ablated_test"
        else:
            new_dir_name = f"{env}-ablated"
        new_problem_dir = utils.PDDL_DIR / "pg3" / new_dir_name / f"seed{FLAGS.seed}"
        os.makedirs(new_problem_dir, exist_ok=True)
        new_problem_file = new_problem_dir / f"task{i}.pddl"
        with open(new_problem_file, "w", encoding="utf-8") as f:
            f.write(new_problem_str)
        print(f"Wrote out to {new_problem_file}")


def _get_domain_substitutions(task: Task):
    substitutions: Dict[str, str] = {}
    # Replace the domain name. Special case the matching because the domain name
    # is sometimes shared in other aspects of the domain or task.
    substitutions[f"(domain {task.domain_name})"] = "(domain my-pddl-domain)"
    substitutions[f"(:domain {task.domain_name})"] = "(:domain my-pddl-domain)"
    # Replace the type names.
    if task.typed:
        for i, old_type_name in enumerate(sorted(task.domain.types)):
            new_type_name = f"type{i}"
            _update_substitutions(substitutions, old_type_name, new_type_name)
    # Replace the predicate names.
    for i, old_predicate_name in enumerate(sorted(task.domain.predicates)):
        # Skip operators that are predicates (PDDLGym parsing quirk).
        if old_predicate_name in task.domain.operators:
            continue
        new_predicate_name = f"predicate{i}"
        _update_substitutions(substitutions, old_predicate_name, new_predicate_name)
    # Replace the operator names.
    for i, old_operator_name in enumerate(sorted(task.domain.operators)):
        new_operator_name = f"operator{i}"
        _update_substitutions(substitutions, old_operator_name, new_operator_name)
    # Replace all of the variables in the domain file.
    # Regex pattern to match substrings starting with a question mark
    # and followed by any characters (including spaces, new lines, and parentheses).
    pattern = r"\?[\s\S]*?(?=\s|$|\n|\(|\))"
    matches = set(re.findall(pattern, task.domain_str))
    for i, old_var_name in enumerate(sorted(matches)):
        new_var_name = f"?v{i}"
        _update_substitutions(substitutions, old_var_name, new_var_name)
    return substitutions


def _get_task_substitutions(
    task: Task, domain_substitutions: Dict[str, str], task_num: int
) -> Dict[str, str]:
    task_substitutions = domain_substitutions.copy()
    # Replace the problem name.
    old_problem_name = task.problem_name
    new_problem_name = f"my-problem-{task_num}"
    _update_substitutions(task_substitutions, old_problem_name, new_problem_name)
    # Replace the object names.
    for i, obj in enumerate(sorted(task.problem.objects)):
        old_obj_name = obj.name
        new_obj_name = f"object{i}"
        _update_substitutions(task_substitutions, old_obj_name, new_obj_name)
    return task_substitutions


def _update_substitutions(subs: Dict[str, str], old_name: str, new_name: str) -> None:
    assert old_name not in subs, f"{old_name} already in sub keys."
    assert new_name not in subs.values(), f"{new_name} already in sub values."
    subs[old_name] = new_name


def _apply_substitutions(old_str: str, substitutions: Dict[str, str]) -> str:
    lefts = [" ", "\n", "\t", "("]
    rights = [" ", "\n", "\t", ")"]
    new_str = old_str
    for left in lefts:
        for right in rights:
            for old, new in substitutions.items():
                wrapped_old = left + old + right
                wrapped_new = left + new + right
                new_str = new_str.replace(wrapped_old, wrapped_new)
    return new_str


def _validate_transformed_task(new_task: Task, old_task: Task) -> None:
    new_plan, _ = utils.run_fastdownward_planning(new_task, alias="seq-opt-lmcut")
    old_plan, _ = utils.run_fastdownward_planning(old_task, alias="seq-opt-lmcut")
    assert len(new_plan) == len(old_plan)


if __name__ == "__main__":
    _main()

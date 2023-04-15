"""Tests for genplan.py."""

import time

from llm_genplan import utils
from llm_genplan.envs import create_tasks
from llm_genplan.flags import FLAGS
from llm_genplan.genplan import GeneralizedPlan, run_genplan_on_task


def test_genplan():
    """Tests for generalized planning."""
    utils.reset_flags(
        {
            "env": "pyperplan-gripper",
            "num_prompt_tasks": 1,
            "num_extra_train_tasks": 1,
            "num_eval_tasks": 1,
        }
    )

    prompt_tasks, extra_train_tasks, eval_tasks = create_tasks(
        env_name=FLAGS.env,
        num_prompt=FLAGS.num_prompt_tasks,
        num_train=FLAGS.num_extra_train_tasks,
        num_eval=FLAGS.num_eval_tasks,
    )
    assert len(prompt_tasks) == 1
    assert len(extra_train_tasks) == 1
    assert len(eval_tasks) == 1
    task = eval_tasks[0]

    # Successful usage.
    gen_plan_code_str = """
def get_plan(objects, init, goal):
    plan = []
    
    balls_in_rooma = set()
    for atom in init:
        if atom[0] == "at" and atom[2] == "rooma":
            balls_in_rooma.add(atom[1])

    ball_gripper_mapping = {}
    while balls_in_rooma:
        # Pick up balls in rooma
        for gripper in ["left", "right"]:
            if balls_in_rooma:
                ball = balls_in_rooma.pop()
                plan.append(f"(pick {ball} rooma {gripper})")
                ball_gripper_mapping[ball] = gripper
                
        # Move to roomb
        plan.append("(move rooma roomb)")

        # Drop balls in roomb
        for ball, gripper in ball_gripper_mapping.items():
            plan.append(f"(drop {ball} roomb {gripper})")

        # Clear ball_gripper_mapping for next iteration
        ball_gripper_mapping.clear()

        # Move back to rooma
        plan.append("(move roomb rooma)")
    
    # Remove the last "move roomb rooma" action, as it's unnecessary
    plan.pop()

    return plan
"""

    generalized_plan = GeneralizedPlan(gen_plan_code_str)
    success, info = run_genplan_on_task(
        generalized_plan,
        task,
        horizon=FLAGS.horizon,
        timeout=None,
    )
    assert success
    assert info == "Generalized plan succeeded."

    # Test case where code is just garbage.
    gen_plan_code_str = """some hot garbage + bugs"""
    generalized_plan = GeneralizedPlan(gen_plan_code_str)
    success, info = run_genplan_on_task(
        generalized_plan,
        task,
        horizon=FLAGS.horizon,
        timeout=None,
    )
    assert not success
    assert "The code raised the following exception:" in info
    assert "SyntaxError: invalid syntax" in info

    # Test case where code imports something that is not available.
    gen_plan_code_str = """import not_a_real_module"""
    generalized_plan = GeneralizedPlan(gen_plan_code_str)
    success, info = run_genplan_on_task(
        generalized_plan,
        task,
        horizon=FLAGS.horizon,
        timeout=None,
    )
    assert not success
    assert "ModuleNotFoundError: No module named 'not_a_real_module'" in info

    # Test case where code outputs an empty plan.
    gen_plan_code_str = """
def get_plan(objects, init, goal):
    return []
"""
    generalized_plan = GeneralizedPlan(gen_plan_code_str)
    success, info = run_genplan_on_task(
        generalized_plan,
        task,
        horizon=FLAGS.horizon,
        timeout=None,
    )
    assert not success
    assert (
        info
        == """The code failed. It returned the following plan: [].
The goal is not satisfied
(Follow each of:
    (Set (at ball8 roomb) to true)
    and (Set (at ball7 roomb) to true)
    and (Set (at ball6 roomb) to true)
    and (Set (at ball5 roomb) to true)
    and (Set (at ball4 roomb) to true)
    and (Set (at ball3 roomb) to true)
    and (Set (at ball2 roomb) to true)
    and (Set (at ball1 roomb) to true)
)"""
    )

    # Test case where code outputs a plan that is one step away from working.
    gen_plan_code_str = """
def get_plan(objects, init, goal):
    plan = []
    
    balls_in_rooma = set()
    for atom in init:
        if atom[0] == "at" and atom[2] == "rooma":
            balls_in_rooma.add(atom[1])

    ball_gripper_mapping = {}
    while balls_in_rooma:
        # Pick up balls in rooma
        for gripper in ["left", "right"]:
            if balls_in_rooma:
                ball = balls_in_rooma.pop()
                plan.append(f"(pick {ball} rooma {gripper})")
                ball_gripper_mapping[ball] = gripper
                
        # Move to roomb
        plan.append("(move rooma roomb)")

        # Drop balls in roomb
        for ball, gripper in ball_gripper_mapping.items():
            plan.append(f"(drop {ball} roomb {gripper})")

        # Clear ball_gripper_mapping for next iteration
        ball_gripper_mapping.clear()

        # Move back to rooma
        plan.append("(move roomb rooma)")
    
    # Remove the last "move roomb rooma" action, as it's unnecessary
    plan.pop()

    # NOTE: Remove one more action for the sake of doing this test.
    plan.pop()

    return plan
"""
    generalized_plan = GeneralizedPlan(gen_plan_code_str)
    success, info = run_genplan_on_task(
        generalized_plan,
        task,
        horizon=FLAGS.horizon,
        timeout=None,
    )
    assert not success
    assert info == (
        "The code failed. It returned the following plan: "
        "['(pick ball4 rooma left)', '(pick ball8 rooma right)', '(move rooma roomb)', "
        "'(drop ball4 roomb left)', '(drop ball8 roomb right)', '(move roomb rooma)', "
        "'(pick ball3 rooma left)', '(pick ball1 rooma right)', '(move rooma roomb)', "
        "'(drop ball3 roomb left)', '(drop ball1 roomb right)', '(move roomb rooma)', "
        "'(pick ball5 rooma left)', '(pick ball7 rooma right)', '(move rooma roomb)', "
        "'(drop ball5 roomb left)', '(drop ball7 roomb right)', '(move roomb rooma)', "
        "'(pick ball2 rooma left)', '(pick ball6 rooma right)', '(move rooma roomb)', "
        "'(drop ball2 roomb left)'].\n"
        "The goal is not satisfied\n"
        "(Set (at ball6 roomb) to true)"
    )

    # Test case where a completely invalid action is returned.
    gen_plan_code_str = """
def get_plan(objects, init, goal):
    return ['(not-a-real-action ball4 rooma left)']
"""
    generalized_plan = GeneralizedPlan(gen_plan_code_str)
    success, info = run_genplan_on_task(
        generalized_plan,
        task,
        horizon=FLAGS.horizon,
        timeout=None,
    )
    assert not success
    assert (
        info
        == """The code returned this plan: ['(not-a-real-action ball4 rooma left)']
However, the action (not-a-real-action ball4 rooma left) is invalid at step 0.
NOTE: the valid operators are: (drop ?obj ?room ?gripper) (move ?from ?to) (pick ?obj ?room ?gripper)."""  # pylint: disable=line-too-long
    )

    # Test case where an action has arguments in the wrong order.
    gen_plan_code_str = """
def get_plan(objects, init, goal):
    return ['(pick rooma ball4 left)']
"""
    generalized_plan = GeneralizedPlan(gen_plan_code_str)
    success, info = run_genplan_on_task(
        generalized_plan,
        task,
        horizon=FLAGS.horizon,
        timeout=None,
    )
    assert not success
    assert info == (
        "The code failed. It returned the following plan: "
        "['(pick rooma ball4 left)'].\n"
        """(pick rooma ball4 left) has an unsatisfied precondition at time 0
(Follow each of:
    (Set (ball rooma) to true)
    and (Set (room ball4) to true)
    and (Set (at rooma ball4) to true)
    and (Set (at-robby ball4) to true)
)"""
    )

    # Test case where get_plan() returns None.
    gen_plan_code_str = """
def get_plan(objects, init, goal):
    return None
"""
    generalized_plan = GeneralizedPlan(gen_plan_code_str)
    success, info = run_genplan_on_task(
        generalized_plan,
        task,
        horizon=FLAGS.horizon,
        timeout=None,
    )
    assert not success
    assert info == "The code returned None, which is not a list of actions."

    # Test case where get_plan() times out.
    gen_plan_code_str = """
def get_plan(objects, init, goal):
    x = 0
    while True:
        x += 1
"""
    generalized_plan = GeneralizedPlan(gen_plan_code_str)
    start_time = time.perf_counter()
    success, info = run_genplan_on_task(
        generalized_plan,
        task,
        horizon=FLAGS.horizon,
        timeout=1,
    )
    duration = time.perf_counter() - start_time
    assert not success
    assert (
        "The code was interrupted because it timed out (possible infinite loop)."
        in info
    )
    assert duration < 5  # add some padding

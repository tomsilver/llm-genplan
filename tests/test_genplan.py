"""Tests for genplan.py."""

import time

from llm_genplan import utils
from llm_genplan.envs import create_tasks
from llm_genplan.flags import FLAGS
from llm_genplan.genplan import GeneralizedPlan, run_genplan_on_task


def test_genplan():
    """Tests for generalized planning."""
    # pylint: disable=line-too-long
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
    balls_in_rooma = sorted(balls_in_rooma)  # sort for determinism

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
    success, info, metrics = run_genplan_on_task(
        generalized_plan,
        task,
        horizon=FLAGS.horizon,
        timeout=None,
    )
    assert success, info
    assert info == "Generalized plan succeeded."

    # Test case where code is just garbage.
    gen_plan_code_str = """some hot garbage + bugs"""
    generalized_plan = GeneralizedPlan(gen_plan_code_str)
    success, info, metrics = run_genplan_on_task(
        generalized_plan,
        task,
        horizon=FLAGS.horizon,
        timeout=None,
    )
    assert not success
    assert "The code raised the following exception:" in info
    assert "SyntaxError: invalid syntax" in info
    assert metrics["python-exception"] == 1

    # Test case where code imports something that is not available.
    gen_plan_code_str = """import not_a_real_module"""
    generalized_plan = GeneralizedPlan(gen_plan_code_str)
    success, info, metrics = run_genplan_on_task(
        generalized_plan,
        task,
        horizon=FLAGS.horizon,
        timeout=None,
    )
    assert not success
    assert "ModuleNotFoundError: No module named 'not_a_real_module'" in info
    assert metrics["python-exception"] == 1

    # Test case where code outputs an empty plan.
    gen_plan_code_str = """
def get_plan(objects, init, goal):
    return []
"""
    generalized_plan = GeneralizedPlan(gen_plan_code_str)
    success, info, metrics = run_genplan_on_task(
        generalized_plan,
        task,
        horizon=FLAGS.horizon,
        timeout=None,
    )
    assert not success
    assert (
        info
        == "Given this task:\n(define (problem strips-gripper-x-3)\n   (:domain gripper-strips)\n   (:objects rooma roomb ball8 ball7 ball6 ball5 ball4 ball3 ball2\n             ball1 left right)\n   (:init (room rooma)\n          (room roomb)\n          (ball ball8)\n          (ball ball7)\n          (ball ball6)\n          (ball ball5)\n          (ball ball4)\n          (ball ball3)\n          (ball ball2)\n          (ball ball1)\n          (at-robby rooma)\n          (free left)\n          (free right)\n          (at ball8 rooma)\n          (at ball7 rooma)\n          (at ball6 rooma)\n          (at ball5 rooma)\n          (at ball4 rooma)\n          (at ball3 rooma)\n          (at ball2 rooma)\n          (at ball1 rooma)\n          (gripper left)\n          (gripper right))\n   (:goal (and (at ball8 roomb)\n               (at ball7 roomb)\n               (at ball6 roomb)\n               (at ball5 roomb)\n               (at ball4 roomb)\n               (at ball3 roomb)\n               (at ball2 roomb)\n               (at ball1 roomb))))\nThe code failed. It returned the following plan: [].\nNOTE: The goal is not satisfied\n(Follow each of:\n    (Set (at ball8 roomb) to true)\n    and (Set (at ball7 roomb) to true)\n    and (Set (at ball6 roomb) to true)\n    and (Set (at ball5 roomb) to true)\n    and (Set (at ball4 roomb) to true)\n    and (Set (at ball3 roomb) to true)\n    and (Set (at ball2 roomb) to true)\n    and (Set (at ball1 roomb) to true)\n)"
    )
    assert metrics["operator-semantics-invalid"] == 1

    # Test case where code outputs a plan that is one step away from working.
    gen_plan_code_str = """
def get_plan(objects, init, goal):
    plan = []
    
    balls_in_rooma = set()
    for atom in init:
        if atom[0] == "at" and atom[2] == "rooma":
            balls_in_rooma.add(atom[1])
    balls_in_rooma = sorted(balls_in_rooma)  # sort for determinism

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
    success, info, metrics = run_genplan_on_task(
        generalized_plan,
        task,
        horizon=FLAGS.horizon,
        timeout=None,
    )
    assert not success
    assert (
        info
        == "Given this task:\n(define (problem strips-gripper-x-3)\n   (:domain gripper-strips)\n   (:objects rooma roomb ball8 ball7 ball6 ball5 ball4 ball3 ball2\n             ball1 left right)\n   (:init (room rooma)\n          (room roomb)\n          (ball ball8)\n          (ball ball7)\n          (ball ball6)\n          (ball ball5)\n          (ball ball4)\n          (ball ball3)\n          (ball ball2)\n          (ball ball1)\n          (at-robby rooma)\n          (free left)\n          (free right)\n          (at ball8 rooma)\n          (at ball7 rooma)\n          (at ball6 rooma)\n          (at ball5 rooma)\n          (at ball4 rooma)\n          (at ball3 rooma)\n          (at ball2 rooma)\n          (at ball1 rooma)\n          (gripper left)\n          (gripper right))\n   (:goal (and (at ball8 roomb)\n               (at ball7 roomb)\n               (at ball6 roomb)\n               (at ball5 roomb)\n               (at ball4 roomb)\n               (at ball3 roomb)\n               (at ball2 roomb)\n               (at ball1 roomb))))\nThe code failed. It returned the following plan: ['(pick ball8 rooma left)', '(pick ball7 rooma right)', '(move rooma roomb)', '(drop ball8 roomb left)', '(drop ball7 roomb right)', '(move roomb rooma)', '(pick ball6 rooma left)', '(pick ball5 rooma right)', '(move rooma roomb)', '(drop ball6 roomb left)', '(drop ball5 roomb right)', '(move roomb rooma)', '(pick ball4 rooma left)', '(pick ball3 rooma right)', '(move rooma roomb)', '(drop ball4 roomb left)', '(drop ball3 roomb right)', '(move roomb rooma)', '(pick ball2 rooma left)', '(pick ball1 rooma right)', '(move rooma roomb)', '(drop ball2 roomb left)'].\nNOTE: The goal is not satisfied\n(Set (at ball1 roomb) to true)"
    )
    assert metrics["operator-semantics-invalid"] == 1

    # Test case where a completely invalid action is returned.
    gen_plan_code_str = """
def get_plan(objects, init, goal):
    return ['(not-a-real-action ball4 rooma left)']
"""
    generalized_plan = GeneralizedPlan(gen_plan_code_str)
    success, info, metrics = run_genplan_on_task(
        generalized_plan,
        task,
        horizon=FLAGS.horizon,
        timeout=None,
    )
    assert not success
    assert (
        info
        == "Given this task:\n(define (problem strips-gripper-x-3)\n   (:domain gripper-strips)\n   (:objects rooma roomb ball8 ball7 ball6 ball5 ball4 ball3 ball2\n             ball1 left right)\n   (:init (room rooma)\n          (room roomb)\n          (ball ball8)\n          (ball ball7)\n          (ball ball6)\n          (ball ball5)\n          (ball ball4)\n          (ball ball3)\n          (ball ball2)\n          (ball ball1)\n          (at-robby rooma)\n          (free left)\n          (free right)\n          (at ball8 rooma)\n          (at ball7 rooma)\n          (at ball6 rooma)\n          (at ball5 rooma)\n          (at ball4 rooma)\n          (at ball3 rooma)\n          (at ball2 rooma)\n          (at ball1 rooma)\n          (gripper left)\n          (gripper right))\n   (:goal (and (at ball8 roomb)\n               (at ball7 roomb)\n               (at ball6 roomb)\n               (at ball5 roomb)\n               (at ball4 roomb)\n               (at ball3 roomb)\n               (at ball2 roomb)\n               (at ball1 roomb))))\nThe code returned this plan: ['(not-a-real-action ball4 rooma left)']\nHowever, the action (not-a-real-action ball4 rooma left) is invalid at step 0.\nNOTE: the valid operators are: (drop ?obj ?room ?gripper) (move ?from ?to) (pick ?obj ?room ?gripper)."
    )
    assert metrics["operator-syntax-invalid"] == 1

    # Test case where an action has arguments in the wrong order.
    gen_plan_code_str = """
def get_plan(objects, init, goal):
    return ['(pick rooma ball4 left)']
"""
    generalized_plan = GeneralizedPlan(gen_plan_code_str)
    success, info, metrics = run_genplan_on_task(
        generalized_plan,
        task,
        horizon=FLAGS.horizon,
        timeout=None,
    )
    assert not success
    assert (
        info
        == "Given this task:\n(define (problem strips-gripper-x-3)\n   (:domain gripper-strips)\n   (:objects rooma roomb ball8 ball7 ball6 ball5 ball4 ball3 ball2\n             ball1 left right)\n   (:init (room rooma)\n          (room roomb)\n          (ball ball8)\n          (ball ball7)\n          (ball ball6)\n          (ball ball5)\n          (ball ball4)\n          (ball ball3)\n          (ball ball2)\n          (ball ball1)\n          (at-robby rooma)\n          (free left)\n          (free right)\n          (at ball8 rooma)\n          (at ball7 rooma)\n          (at ball6 rooma)\n          (at ball5 rooma)\n          (at ball4 rooma)\n          (at ball3 rooma)\n          (at ball2 rooma)\n          (at ball1 rooma)\n          (gripper left)\n          (gripper right))\n   (:goal (and (at ball8 roomb)\n               (at ball7 roomb)\n               (at ball6 roomb)\n               (at ball5 roomb)\n               (at ball4 roomb)\n               (at ball3 roomb)\n               (at ball2 roomb)\n               (at ball1 roomb))))\nThe code failed. It returned the following plan: ['(pick rooma ball4 left)'].\nNOTE: (pick rooma ball4 left) has an unsatisfied precondition at time 0\n(Follow each of:\n    (Set (ball rooma) to true)\n    and (Set (room ball4) to true)\n    and (Set (at rooma ball4) to true)\n    and (Set (at-robby ball4) to true)\n)"
    )
    assert metrics["operator-semantics-invalid"] == 1

    # Test case where get_plan() returns None.
    gen_plan_code_str = """
def get_plan(objects, init, goal):
    return None
"""
    generalized_plan = GeneralizedPlan(gen_plan_code_str)
    success, info, metrics = run_genplan_on_task(
        generalized_plan,
        task,
        horizon=FLAGS.horizon,
        timeout=None,
    )
    assert not success
    assert (
        info
        == "Given this task:\n(define (problem strips-gripper-x-3)\n   (:domain gripper-strips)\n   (:objects rooma roomb ball8 ball7 ball6 ball5 ball4 ball3 ball2\n             ball1 left right)\n   (:init (room rooma)\n          (room roomb)\n          (ball ball8)\n          (ball ball7)\n          (ball ball6)\n          (ball ball5)\n          (ball ball4)\n          (ball ball3)\n          (ball ball2)\n          (ball ball1)\n          (at-robby rooma)\n          (free left)\n          (free right)\n          (at ball8 rooma)\n          (at ball7 rooma)\n          (at ball6 rooma)\n          (at ball5 rooma)\n          (at ball4 rooma)\n          (at ball3 rooma)\n          (at ball2 rooma)\n          (at ball1 rooma)\n          (gripper left)\n          (gripper right))\n   (:goal (and (at ball8 roomb)\n               (at ball7 roomb)\n               (at ball6 roomb)\n               (at ball5 roomb)\n               (at ball4 roomb)\n               (at ball3 roomb)\n               (at ball2 roomb)\n               (at ball1 roomb))))\nThe code returned None, which is not a list of actions."
    )
    assert metrics["output-not-plan"] == 1

    # Test case where get_plan() times out.
    gen_plan_code_str = """
def get_plan(objects, init, goal):
    x = 0
    while True:
        x += 1
"""
    generalized_plan = GeneralizedPlan(gen_plan_code_str)
    start_time = time.perf_counter()
    success, info, metrics = run_genplan_on_task(
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
    assert metrics["timeout"] == 1

"""Interact with an LLM to get a generalized plan."""

from typing import List

from llm_genplan.structs import GeneralizedPlan, Task


def get_genplan_from_llm(train_tasks: List[Task]) -> GeneralizedPlan:
    """Interact with an LLM to get a generalized plan."""
    # Coming soon
    del train_tasks
    gen_plan_code_str = """def get_plan(objects, init, goal):
    initial_state = set(init)
    actions = []

    def find(predicate, *args):
        for atom in initial_state:
            if atom[0] == predicate and all(a == b for a, b in zip(args, atom[1:])):
                return atom[1:]
        return None

    def find_all(predicate):
        return [atom[1:] for atom in initial_state if atom[0] == predicate]

    def move_to_room(room):
        robby_room = find('at-robby')[0]
        if robby_room != room:
            actions.append(('move', robby_room, room))
            initial_state.discard(('at-robby', robby_room))
            initial_state.add(('at-robby', room))

    def pick_ball(ball, room, gripper):
        actions.append(('pick', ball, room, gripper))
        initial_state.discard(('at', ball, room))
        initial_state.discard(('free', gripper))
        initial_state.add(('carry', ball, gripper))

    def drop_ball(ball, room, gripper):
        actions.append(('drop', ball, room, gripper))
        initial_state.add(('at', ball, room))
        initial_state.add(('free', gripper))
        initial_state.discard(('carry', ball, gripper))

    balls = find_all('ball')
    grippers = find_all('gripper')
    free_grippers = [g[0] for g in find_all('free')]

    for ball, dest_room in [atom[1:] for atom in goal if atom[0] == 'at']:
        if ball in [b[0] for b in balls]:
            ball_room = find('at', ball)[1]
            move_to_room(ball_room)

            gripper = free_grippers.pop()
            pick_ball(ball, ball_room, gripper)

            move_to_room(dest_room)
            drop_ball(ball, dest_room, gripper)

            free_grippers.append(gripper)

    return actions
"""
    return GeneralizedPlan(gen_plan_code_str)

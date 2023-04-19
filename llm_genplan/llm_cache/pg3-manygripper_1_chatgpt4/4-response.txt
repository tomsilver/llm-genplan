def get_plan(objects, init, goal):
    def get_objects_of_type(type_name):
        return [obj for obj in objects if obj.startswith(type_name)]

    def get_location(state, ball):
        for atom in state:
            if atom[0] == 'at' and atom[1] == ball:
                return atom[2]
        return None

    balls = get_objects_of_type('ball')
    rooms = get_objects_of_type('room')
    grippers = get_objects_of_type('gripper')

    robby_location = None
    for atom in init:
        if atom[0] == 'at-robby':
            robby_location = atom[1]
            break

    plan = []
    for ball in balls:
        initial_location = get_location(init, ball)
        goal_location = get_location(goal, ball)

        if goal_location is None:
            continue

        if initial_location != goal_location:
            plan.append(f'(move {robby_location} {initial_location})')
            robby_location = initial_location

            plan.append(f'(pick {ball} {initial_location} {grippers[0]})')

            plan.append(f'(move {robby_location} {goal_location})')
            robby_location = goal_location

            plan.append(f'(drop {ball} {goal_location} {grippers[0]})')

    return plan

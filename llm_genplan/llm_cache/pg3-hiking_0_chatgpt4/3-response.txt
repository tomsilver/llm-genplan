def get_plan(objects, init, goal):
    def find_location(init):
        for atom in init:
            if atom[0] == "at":
                return atom[1]
        return None

    def find_adjacent_trail(current_loc, init):
        for atom in init:
            if atom[0] == "ontrail" and atom[1] == current_loc:
                return atom[2]
        return None

    def is_hill(loc, init):
        for atom in init:
            if atom[0] == "ishill" and atom[1] == loc:
                return True
        return False

    current_loc = find_location(init)
    goal_loc = find_location(goal)
    plan = []

    while current_loc != goal_loc:
        next_loc = find_adjacent_trail(current_loc, init)

        if is_hill(next_loc, init):
            action = f"(climb {current_loc} {next_loc})"
        else:
            action = f"(walk {current_loc} {next_loc})"

        plan.append(action)
        current_loc = next_loc

    return plan

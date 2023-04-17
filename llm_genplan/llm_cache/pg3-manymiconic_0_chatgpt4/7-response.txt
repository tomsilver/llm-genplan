def get_plan(objects, init, goal):
    floors_by_building = {}
    passengers_by_building = {}

    for obj, obj_type in objects:
        if obj_type == "floor":
            building = obj.split("_")[-1]
            if building not in floors_by_building:
                floors_by_building[building] = []
            floors_by_building[building].append(obj)
        elif obj_type == "passenger":
            building = obj.split("_")[-1]
            if building not in passengers_by_building:
                passengers_by_building[building] = []
            passengers_by_building[building].append(obj)

    for building in floors_by_building:
        floors_by_building[building] = sorted(floors_by_building[building])

    origins = {p: f for p, f in (atom[1:] for atom in init if atom[0] == "origin")}
    destins = {p: f for p, f in (atom[1:] for atom in init if atom[0] == "destin")}
    lift_at = {atom[1]: atom for atom in init if atom[0] == "lift-at"}

    plan = []
    boarded = set()

    for building, floors in floors_by_building.items():
        passengers = passengers_by_building[building]
        current_lift_at = lift_at[building]

        for floor in floors + list(reversed(floors)):
            if current_lift_at != floor:
                if current_lift_at < floor:
                    plan.append(f"(up {current_lift_at} {floor})")
                else:
                    plan.append(f"(down {current_lift_at} {floor})")
                current_lift_at = floor

            for passenger in passengers:
                if origins.get(passenger) == floor:
                    plan.append(f"(board {floor} {passenger})")
                    boarded.add(passenger)

                if destins.get(passenger) == floor and passenger in boarded:
                    plan.append(f"(depart {floor} {passenger})")
                    boarded.remove(passenger)

    return plan

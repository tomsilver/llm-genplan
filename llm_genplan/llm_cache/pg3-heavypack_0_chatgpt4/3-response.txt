def extract_heavier_relations(init):
    heavier_relations = set()
    for atom in init:
        if atom[0] == 'heavier':
            heavier_relations.add(atom)
    return heavier_relations

def sort_objects_by_weight(objects, heavier_relations):
    sorted_objects = []
    while len(objects) > 0:
        for obj in objects.copy():
            if all(('heavier', other, obj) not in heavier_relations for other in objects):
                sorted_objects.append(obj)
                objects.remove(obj)
    return sorted_objects

def get_plan(objects, init, goal):
    heavier_relations = extract_heavier_relations(init)
    sorted_objects = sort_objects_by_weight(set(objects), heavier_relations)

    plan = []
    first_object = sorted_objects.pop(0)
    plan.append(f"(pack-first {first_object})")

    for obj in sorted_objects:
        plan.append(f"(stack {first_object} {obj})")
        first_object = obj

    return plan

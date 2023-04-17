def get_plan(objects, init, goal):
    locs = [obj[0] for obj in objects if obj[1] == "loc"]
    papers = [obj[0] for obj in objects if obj[1] == "paper"]
    
    home_base = next(loc for loc in locs if ("ishomebase", loc) in init)
    safe_locs = [loc for loc in locs if ("safe", loc) in init]
    wants_paper = [loc for loc in locs if ("wantspaper", loc) in init]
    
    plan = []
    
    for loc in wants_paper:
        if loc in safe_locs:
            # Pick up a newspaper at the home base
            paper = papers.pop()
            plan.append(f"(pick-up {paper} {home_base})")
            
            # Move to the safe location that wants a newspaper
            plan.append(f"(move {home_base} {loc})")
            
            # Deliver the newspaper to the location
            plan.append(f"(deliver {paper} {loc})")
            
            # Move back to the home base
            plan.append(f"(move {loc} {home_base})")
    
    return plan

from pddlgym.parser import PDDLDomainParser, PDDLProblemParser
from pddlgym.structs import LiteralConjunction
import pddlgym
import os
import numpy as np
from itertools import count
import heapq

PDDLDIR = os.path.join(os.path.dirname(pddlgym.__file__), "pddl")

I, G, W, P, X, H = range(6)

"""
Questions to consider:
    1. Do we allow adjacent blocks to be a path?
        a. Yes?
    2. Any requirements for how water is distributed across the non-path/non-rock areas? (or can we just set a probability between water and dirt)
        b. Random 50/50 b/w water and non-path/non-water
    3. Is there a requirement for rocks to be on the path? (or can we similarly just set a probability between marked trail and rocks)
        c. Random 20% chance of rocks
"""

def generate_random_grid(grid_height, grid_width):
    I_row = np.random.randint(0, grid_height)
    I_col = np.random.randint(0, grid_width)

    G_row = np.random.randint(0, grid_height)
    G_col = np.random.randint(0, grid_width)
    while (G_row, G_col) == (I_row, I_col):
        G_row = np.random.randint(0, grid_height)
        G_col = np.random.randint(0, grid_width)

    random_path =  random_grid_walk((I_row, I_col), (G_row, G_col), set(), grid_height, grid_width, None)
    assert random_path

    remaining_coords = {(r, c) for r in range(grid_height) for c in range(grid_width)} - set(random_path)

    grid = [[None for c in range(grid_width)] for r in range(grid_height)]

    for non_path_coord in remaining_coords:
        loc_prob = np.random.uniform()
        if loc_prob <= 0.5:
            grid[non_path_coord[0]][non_path_coord[1]] = X
        else:
            grid[non_path_coord[0]][non_path_coord[1]] = W

    last_was_hill = False
    for i, path_coord in enumerate(random_path):
        loc_prob = np.random.uniform()
        if path_coord == (I_row, I_col):
            grid[path_coord[0]][path_coord[1]] = I
        elif path_coord == (G_row, G_col): 
            grid[path_coord[0]][path_coord[1]] = G
        elif i > 1 and not last_was_hill and loc_prob <= 0.2:
            grid[path_coord[0]][path_coord[1]] = H
            last_was_hill = True
        else:
            grid[path_coord[0]][path_coord[1]] = P
    
    #print("Random path", sorted(random_path))
    #print("Reamaining_coords", sorted(remaining_coords))

    for r in range(grid_height):
        for c in range(grid_width):
            assert grid[r][c] != None
    
    # for r in grid:
    #     print(r)
    return grid


def random_grid_walk(currCoords, goalCoords, visited, grid_height, grid_width, previousCoords):
    if currCoords == goalCoords:
        return [currCoords]
    
    for delta in np.random.permutation([[0, 1], [1, 0], [0, -1], [-1, 0]]):
        new_coord = (currCoords[0] + delta[0], currCoords[1] + delta[1])
        if new_coord[0] < 0 or new_coord[0] >= grid_height or new_coord[1] < 0 or new_coord[1] >= grid_width: 
            #print("Out of bounds")
            continue

        if new_coord in visited:
            #print("Already visited")
            continue

        adjacent_excluding_previous = {(currCoords[0] + adj_delta[0], currCoords[1] + adj_delta[1]) for adj_delta in [[0, 1], [1, 0], [0, -1], [-1, 0]]} - {previousCoords}
        adjacent_hit = False
        for adjacent_coord in adjacent_excluding_previous:
            if adjacent_coord in visited:
                adjacent_hit = True
        if adjacent_hit:
            #print("Adjacent hit")
            continue

        if not reachable(new_coord, goalCoords, visited | {currCoords}, grid_height, grid_width):
            #print("Not reachable from here")
            continue
                        
        grid_walk_from_child = random_grid_walk(new_coord, goalCoords, visited | {currCoords}, grid_height, grid_width, currCoords)
        if grid_walk_from_child != None:
            return [currCoords] + grid_walk_from_child

    return None


def reachable(currCoords, goalCoords, prev_visited, grid_height, grid_width):
    queue = [(currCoords, prev_visited.copy())]
    coord_queue = [currCoords]
    visited = prev_visited.copy()

    while len(queue) > 0:
        curr, curr_visited = queue[0]
        del queue[0]
        del coord_queue[0]

        if curr == goalCoords:
            return True

        for delta in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            newC = (curr[0] + delta[0], curr[1] + delta[1])
            if newC[0] < 0 or newC[0] >= grid_height or newC[1] < 0 or newC[1] >= grid_width: 
                #print("Out of bounds")
                continue

            if newC in visited or newC in coord_queue:
                #print("Already visited or in queue")
                continue

            adjacent_excluding_previous = {(newC[0] + adj_delta[0], newC[1] + adj_delta[1]) for adj_delta in [[0, 1], [1, 0], [0, -1], [-1, 0]]} - {curr}
            adjacent_hit = False
            for adjacent_coord in adjacent_excluding_previous:
                if adjacent_coord in curr_visited:
                    adjacent_hit = True
            if adjacent_hit:
                #print("Adjacent hit")
                continue

            queue.append((newC, curr_visited | {curr}))
            coord_queue.append(newC)

    return False




def grid_A_star(grid_weights, Irow, Icol, Grow, Gcol):
    for row in grid_weights:
        print(row)
    print(Irow, Icol, Grow, Gcol)

    queue = []
    visited = set()
    distances = {}
    heapq.heappush(queue, (0, (Irow, Icol)))
    predecessors = {}

    while heapq:
        dist, coords = heapq.heappop(queue)
        print(dist, coords)
        if coords == (Grow, Gcol):
            break
        if coords in visited:
            continue

        visited.add(coords)

        for delta in ([0, 1], [1, 0], [0, -1], [-1, 0]):
            new_coord = (coords[0] + delta[0], coords[1] + delta[1])
            if new_coord[0] < 0 or new_coord[0] >= len(grid_weights) or new_coord[1] < 0 or new_coord[1] >= len(grid_weights): 
                continue

            new_dist = dist + grid_weights[new_coord[0]][new_coord[1]]
            if new_coord not in distances.keys() or new_dist < distances[new_coord]:
                distances[new_coord] = new_dist
                predecessors[new_coord] = coords
                heapq.heappush(queue, (new_dist, new_coord))
    
    curr_coord = (Grow, Gcol)
    path = [curr_coord]
    while curr_coord != (Irow, Icol):
        path.append(predecessors[curr_coord])
        curr_coord = predecessors[curr_coord]
    
    return path


#TRAIN_GRIDS = [generate_random_grid(10, 10) for i in range(10)]
#TEST_GRIDS = [generate_random_grid(10, 10) for i in range(10)]

def create_problem(grid, domain, problem_dir, problem_outfile):
    # Create location objects
    loc_type = domain.types['loc']
    objects = set()
    grid_locs = np.empty(grid.shape, dtype=object)
    for r in range(grid.shape[0]):
        for c in range(grid.shape[1]):
            obj = loc_type(f'r{r}_c{c}')
            objects.add(obj)
            grid_locs[r, c] = obj

    initial_state = set()

    # Add at, isWater, isHill
    at = domain.predicates['at']
    isWater = domain.predicates['iswater']
    isHill = domain.predicates['ishill']
    for r in range(grid.shape[0]):
        for c in range(grid.shape[1]):
            obj = grid_locs[r, c]
            if grid[r, c] == I:
                initial_state.add(at(obj))
            elif grid[r, c] == W:
                initial_state.add(isWater(obj))
            elif grid[r, c] == H:
                initial_state.add(isHill(obj))

    # Add adjacent
    adjacent = domain.predicates['adjacent']

    def get_neighbors(r, c):
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr = r + dr
            nc = c + dc
            if 0 <= nr < grid.shape[0] and 0 <= nc < grid.shape[1]:
                yield (nr, nc)

    for r in range(grid.shape[0]):
        for c in range(grid.shape[1]):    
            obj = grid_locs[r, c]
            for (nr, nc) in get_neighbors(r, c):
                nobj = grid_locs[nr, nc]
                initial_state.add(adjacent(obj, nobj))

    # Add onTrail
    onTrail = domain.predicates['ontrail']

    # Get the path
    path = []
    r, c = np.argwhere(grid == I)[0]
    while True:
        path.append((r, c))
        if grid[r, c] == G:
            break
        for (nr, nc) in get_neighbors(r, c):
            if (nr, nc) in path:
                continue
            if grid[nr, nc] in [P, G, H]:
                r, c = nr, nc
                break
        else:
            raise Exception("Should not happen")

    for (r, c), (nr, nc) in zip(path[:-1], path[1:]):
        obj = grid_locs[r, c]
        nobj = grid_locs[nr, nc]
        initial_state.add(onTrail(obj, nobj))

    # Goal
    goal_rcs = np.argwhere(grid == G)
    assert len(goal_rcs) == 1
    goal_r, goal_c = goal_rcs[0]
    goal_obj = grid_locs[goal_r, goal_c]
    goal = LiteralConjunction([at(goal_obj)])

    filepath = os.path.join(problem_dir, problem_outfile)

    PDDLProblemParser.create_pddl_file(
        filepath,
        objects=objects,
        initial_state=initial_state,
        problem_name="hiking",
        domain_name=domain.domain_name,
        goal=goal,
        fast_downward_order=True,
    )
    print("Wrote out to {}.".format(filepath))

def generate_problems():
    domain = PDDLDomainParser(os.path.join(PDDLDIR, "hiking.pddl"),
        expect_action_preds=False,
        operators_as_actions=True)

    for seed in range(10):
        np.random.seed(seed)

        # Train problems
        # Number of training problems: 5 
        # Grid height: 3 - 5
        # Grid width: 3 - 5
        for problem_idx in range(10):
            problem_dir = "hiking/seed{}".format(seed)
            problem_outfile = "problem{}.pddl".format(problem_idx)

            grid_height = np.random.randint(8, 10)
            grid_width = np.random.randint(8, 10)
            grid = np.array(generate_random_grid(grid_height, grid_width))
            create_problem(grid, domain, problem_dir, problem_outfile)

        for problem_idx in range(30):
            problem_dir = "hiking_test/seed{}".format(seed)
            problem_outfile = "problem{}.pddl".format(problem_idx)

            grid_height = np.random.randint(10, 12)
            grid_width = np.random.randint(10, 12)
            grid = np.array(generate_random_grid(grid_height, grid_width))
            create_problem(grid, domain, problem_dir, problem_outfile)

if __name__ == "__main__":
    generate_problems()

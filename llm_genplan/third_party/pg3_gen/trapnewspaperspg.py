from pddlgym.parser import PDDLDomainParser, PDDLProblemParser
from pddlgym.structs import LiteralConjunction
import pddlgym
import os
import numpy as np
from itertools import count


PDDLDIR = os.path.join(os.path.dirname(pddlgym.__file__), "pddl")


def sample_problem(domain, problem_dir, problem_outfile, num_locs,
                   num_want_locs, num_newspapers):
    loc_type = domain.types['loc']
    paper_type = domain.types['paper']
    at = domain.predicates['at']
    isHomeBase = domain.predicates['ishomebase']
    wantsPaper = domain.predicates['wantspaper']
    safe = domain.predicates['safe']
    unpacked = domain.predicates['unpacked']
    satisfied = domain.predicates['satisfied']

    # Create objects and state
    state = set()
    objects = set()
    home_loc = None

    all_loc_nums = [i for i in range(1, num_locs)]
    target_loc_nums = np.random.choice(all_loc_nums, num_want_locs, replace = False)
    # print("Target loc nums", target_loc_nums)

    target_locs = []
    # Add locations
    for loc_idx in range(num_locs):
        loc = loc_type(f"loc-{loc_idx}")
        objects.add(loc)
        # home
        if loc_idx == 0:
            state.add(isHomeBase(loc))
            state.add(at(loc))
            state.add(safe(loc))
            home_loc = loc
        # wants paper
        if loc_idx in target_loc_nums:
            state.add(wantsPaper(loc))
            state.add(safe(loc))
            target_locs.append(loc)

    # Add papers
    for paper_idx in range(num_newspapers):
        paper = paper_type(f"paper-{paper_idx}")
        objects.add(paper)
        state.add(unpacked(paper))

    # print("Target locs", target_locs)
    # Create goal
    goal_lits = [satisfied(loc) for loc in target_locs]
    goal = LiteralConjunction(goal_lits)
    # print("Goal", goal, "\n")

    filepath = os.path.join(problem_dir, problem_outfile)

    PDDLProblemParser.create_pddl_file(
        filepath,
        objects=objects,
        initial_state=state,
        problem_name="newspaper",
        domain_name=domain.domain_name,
        goal=goal,
        fast_downward_order=True,
    )
    print("Wrote out to {}.".format(filepath))

def generate_problems():
    domain = PDDLDomainParser(os.path.join(PDDLDIR, "trapnewspapers.pddl"),
        expect_action_preds=False,
        operators_as_actions=True)


    for seed in range(10):
        np.random.seed(seed)
        train_problem_dir="pcp/trapnewspapers/seed{}".format(seed)
        test_problem_dir = "pcp/trapnewspapers_test/seed{}".format(seed)

        #Training problems
        #Number of locations: 5 - 10
        #Number of want/safe locs: 2 - 5
        #Number of newspapers: # of safe locs + np.random.randint(0, 1)
        for problem_idx in range(5):
            problem_dir = train_problem_dir
            if not os.path.exists(os.path.join(problem_dir)):
                os.makedirs(os.path.join(problem_dir))
            problem_outfile = "problem{}.pddl".format(problem_idx)

            num_locs = np.random.randint(5, 10)
            num_want_locs = np.random.randint(2, 5)
            num_newspapers = num_want_locs + np.random.randint(0, 1)
            sample_problem(domain, problem_dir, problem_outfile, num_locs, num_want_locs, num_newspapers)

        #Test problems
        #Number of locations: 30 - 40
        #Number of want/safe locs: 20 - 30
        #Number of newspapers: # of safe locs + np.random.randint(0, 10)
        for problem_idx in range(30):
            problem_dir = test_problem_dir
            if not os.path.exists(os.path.join(problem_dir)):
                os.makedirs(os.path.join(problem_dir))
            problem_outfile = "problem{}.pddl".format(problem_idx)

            num_locs = np.random.randint(30, 40)
            num_want_locs = np.random.randint(20, 30)
            num_newspapers = num_want_locs + np.random.randint(0, 10)
            sample_problem(domain, problem_dir, problem_outfile, num_locs, num_want_locs, num_newspapers)



if __name__ == "__main__":
    generate_problems()
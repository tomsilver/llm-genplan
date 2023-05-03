import random
import os


def _get_str(num_floors, num_pass, num_buildings):
    mystr = "(define (problem miconicprob)\n\t(:domain miconic)\n\t(:objects\n"
    for bldg in range(num_buildings):
        for i in range(num_floors):
            mystr += "\t\tf{}_b{} - floor\n".format(i, bldg)
        for i in range(num_pass):
            mystr += "\t\tp{}_b{} - passenger\n".format(i, bldg)
    mystr += "\t)\n\n(:init\n"
    for bldg in range(num_buildings):
        for i in range(num_floors):
            for j in range(i+1, num_floors):
                mystr += "\t(above f{}_b{} f{}_b{})\n".format(i, bldg, j, bldg)
    mystr += "\n"
    for bldg in range(num_buildings):
        free_floors = list(range(num_floors))
        for i in range(num_pass):
            orig = random.choice(free_floors)
            free_floors.remove(orig)
            dest = random.choice([f for f in range(num_floors) if f != orig])
            mystr += "\t(origin p{}_b{} f{}_b{})\n".format(i, bldg, orig, bldg)
            mystr += "\t(destin p{}_b{} f{}_b{})\n".format(i, bldg, dest, bldg)
    mystr += "\n"
    for bldg in range(num_buildings):
        lift_orig = random.randint(0, num_floors-1)
        mystr += "\t(lift-at f{}_b{})\n".format(lift_orig, bldg)
    mystr += ")\n\n(:goal (and\n"
    for bldg in range(num_buildings):
        for i in range(num_pass):
            mystr += "\t(served p{}_b{})\n".format(i, bldg)
    mystr += "))"
    return mystr


def _main():
    print(os.listdir())
    num_seeds = 10
    for s in range(num_seeds):
        random.seed(s)
        # Train problems
        for i in range(10):
            num_floors = random.randint(5, 10)
            num_pass = random.randint(1, 5)
            num_buildings = random.randint(1, 2)
            mystr = _get_str(num_floors, num_pass, num_buildings)
            filename = "manymiconic/seed{}/problem{}.pddl".format(s, i)
            os.makedirs(os.path.dirname(filename), exist_ok=True)
            with open(filename, "w") as f:
                f.write(mystr)
        # Test problems
        for i in range(30):
            num_floors = random.randint(10, 20)
            num_pass = random.randint(1, 10)
            num_buildings = random.randint(1, 5)
            mystr = _get_str(num_floors, num_pass, num_buildings)
            filename = "manymiconic_test/seed{}/problem{}.pddl".format(s, i)
            os.makedirs(os.path.dirname(filename), exist_ok=True)
            with open(filename, "w") as f:
                f.write(mystr)



if __name__ == "__main__":
    _main()

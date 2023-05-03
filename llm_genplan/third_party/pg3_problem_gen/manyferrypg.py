import random
import os


def _get_str(num_locs, num_cars):
    mystr = "(define (problem ferryprob)\n\t(:domain ferry)\n\t(:objects\n"
    for loc in range(num_locs):
        mystr += "\t\tl{}\n".format(loc)
    for car in range(num_cars):
        mystr += "\t\tc{}\n".format(car)

    mystr += "\t)\n\n(:init\n"
    for loc in range(num_locs):
        mystr += "\t(location l{})\n".format(loc)
    for car in range(num_cars):
        mystr += "\t(car c{})\n".format(car)
    for locA in range(num_locs):
        for locB in range(num_locs):
            if locA != locB:
                mystr += "\t(not-eq l{} l{})\n".format(locA, locB)
    mystr += "\t(empty-ferry)\n"
    
    for car in range(num_cars):
        car_origin = random.randint(0, num_locs-1)
        mystr += "\t(at c{} l{})\n".format(car, car_origin)


    ferry_origin = random.randint(0, num_locs-1)
    mystr += "\t(at-ferry l{})\n".format(ferry_origin)

    mystr += ")\n\n(:goal (and\n"

    for car in range(num_cars):
        car_dest = random.randint(0, num_locs-1)
        mystr += "\t(at c{} l{})\n".format(car, car_dest)

    mystr += ")))"
    return mystr


def _main():
    num_seeds = 10
    for s in range(num_seeds):
        random.seed(s)
        # Train problems
        # Number of training problems: 10 
        # Number of locations: 10 - 15
        # Number of cars: 3 - 5
        for i in range(10):
            num_locs = random.randint(10, 15)
            num_cars = random.randint(3, 5)
            mystr = _get_str(num_locs, num_cars)
            filename = "manyferry/seed{}/problem{}.pddl".format(s, i)
            os.makedirs(os.path.dirname(filename), exist_ok=True)
            with open(filename, "w") as f:
                f.write(mystr)
        # Test problems
        # Number of test problems: 30 
        # Number of locations: 20 - 30
        # Number of cars: 10 - 20
        for i in range(30):
            num_locs = random.randint(20, 30)
            num_cars = random.randint(10, 20)
            mystr = _get_str(num_locs, num_cars)
            filename = "manyferry_test/seed{}/problem{}.pddl".format(s, i)
            os.makedirs(os.path.dirname(filename), exist_ok=True)
            with open(filename, "w") as f:
                f.write(mystr)



if __name__ == "__main__":
    _main()

(define (problem my-problem-8)
	(:domain my-pddl-domain)
	(:objects object0 object1 object2 object3 object4)

(:init
    (predicate0)
    (predicate6 object0)
    (predicate6 object1)
    (predicate6 object2)
    (predicate6 object3)
    (predicate6 object4)
    (predicate1 object3 object1)
    (predicate1 object3 object2)
    (predicate1 object3 object0)
    (predicate1 object3 object4)
    (predicate1 object1 object2)
    (predicate1 object1 object0)
    (predicate1 object1 object4)
    (predicate1 object2 object0)
    (predicate1 object2 object4)
    (predicate1 object0 object4)
)

(:goal (and (predicate4 object0) (predicate4 object1) (predicate4 object2) (predicate4 object3) (predicate4 object4)))
)

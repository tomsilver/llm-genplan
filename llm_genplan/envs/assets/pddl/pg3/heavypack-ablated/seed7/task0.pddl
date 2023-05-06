(define (problem my-problem-0)
	(:domain my-pddl-domain)
	(:objects object0 object1 object2)

(:init
    (predicate0)
    (predicate6 object0)
    (predicate6 object1)
    (predicate6 object2)
    (predicate1 object0 object1)
    (predicate1 object0 object2)
    (predicate1 object1 object2)
)

(:goal (and (predicate4 object0) (predicate4 object1) (predicate4 object2)))
)

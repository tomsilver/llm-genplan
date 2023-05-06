(define (problem my-problem-9)
	(:domain my-pddl-domain)
	(:objects
		object0 - type0
		object1 - type0
		object2 - type0
		object3 - type0
		object4 - type0
		object5 - type0
		object6 - type0
		object7 - type2
	)

(:init
	(predicate0 object0 object1)
	(predicate0 object0 object2)
	(predicate0 object0 object3)
	(predicate0 object0 object4)
	(predicate0 object0 object5)
	(predicate0 object0 object6)
	(predicate0 object1 object2)
	(predicate0 object1 object3)
	(predicate0 object1 object4)
	(predicate0 object1 object5)
	(predicate0 object1 object6)
	(predicate0 object2 object3)
	(predicate0 object2 object4)
	(predicate0 object2 object5)
	(predicate0 object2 object6)
	(predicate0 object3 object4)
	(predicate0 object3 object5)
	(predicate0 object3 object6)
	(predicate0 object4 object5)
	(predicate0 object4 object6)
	(predicate0 object5 object6)

	(predicate7 object7 object5)
	(predicate4 object7 object0)

	(predicate6 object3)
)

(:goal (and
	(predicate8 object7)
))
)

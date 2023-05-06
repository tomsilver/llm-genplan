(define (problem my-problem-1)
	(:domain my-pddl-domain)
	(:objects
		object0 - type0
		object1 - type0
		object2 - type0
		object3 - type0
		object4 - type0
		object5 - type2
		object6 - type2
		object7 - type2
		object8 - type2
		object9 - type2
	)

(:init
	(predicate0 object0 object1)
	(predicate0 object0 object2)
	(predicate0 object0 object3)
	(predicate0 object0 object4)
	(predicate0 object1 object2)
	(predicate0 object1 object3)
	(predicate0 object1 object4)
	(predicate0 object2 object3)
	(predicate0 object2 object4)
	(predicate0 object3 object4)

	(predicate7 object5 object0)
	(predicate4 object5 object2)
	(predicate7 object6 object4)
	(predicate4 object6 object2)
	(predicate7 object7 object1)
	(predicate4 object7 object4)
	(predicate7 object8 object2)
	(predicate4 object8 object0)
	(predicate7 object9 object3)
	(predicate4 object9 object4)

	(predicate6 object1)
)

(:goal (and
	(predicate8 object5)
	(predicate8 object6)
	(predicate8 object7)
	(predicate8 object8)
	(predicate8 object9)
))
)

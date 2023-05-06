(define (problem my-problem-0)
	(:domain my-pddl-domain)
	(:objects
		object0 - type0
		object1 - type0
		object2 - type0
		object3 - type0
		object4 - type0
		object5 - type0
		object6 - type0
		object7 - type0
		object8 - type2
		object9 - type2
		object10 - type2
		object11 - type2
	)

(:init
	(predicate0 object0 object1)
	(predicate0 object0 object2)
	(predicate0 object0 object3)
	(predicate0 object0 object4)
	(predicate0 object0 object5)
	(predicate0 object0 object6)
	(predicate0 object0 object7)
	(predicate0 object1 object2)
	(predicate0 object1 object3)
	(predicate0 object1 object4)
	(predicate0 object1 object5)
	(predicate0 object1 object6)
	(predicate0 object1 object7)
	(predicate0 object2 object3)
	(predicate0 object2 object4)
	(predicate0 object2 object5)
	(predicate0 object2 object6)
	(predicate0 object2 object7)
	(predicate0 object3 object4)
	(predicate0 object3 object5)
	(predicate0 object3 object6)
	(predicate0 object3 object7)
	(predicate0 object4 object5)
	(predicate0 object4 object6)
	(predicate0 object4 object7)
	(predicate0 object5 object6)
	(predicate0 object5 object7)
	(predicate0 object6 object7)

	(predicate7 object8 object4)
	(predicate4 object8 object5)
	(predicate7 object9 object3)
	(predicate4 object9 object4)
	(predicate7 object10 object2)
	(predicate4 object10 object4)
	(predicate7 object11 object5)
	(predicate4 object11 object4)

	(predicate6 object3)
)

(:goal (and
	(predicate8 object8)
	(predicate8 object9)
	(predicate8 object10)
	(predicate8 object11)
))
)

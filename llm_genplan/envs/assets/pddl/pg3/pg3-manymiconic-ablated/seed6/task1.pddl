(define (problem my-problem-1)
	(:domain my-pddl-domain)
	(:objects
		object0 - type0
		object2 - type0
		object4 - type0
		object6 - type0
		object8 - type0
		object10 - type0
		object12 - type0
		object14 - type2
		object1 - type0
		object3 - type0
		object5 - type0
		object7 - type0
		object9 - type0
		object11 - type0
		object13 - type0
		object15 - type2
	)

(:init
	(predicate0 object0 object2)
	(predicate0 object0 object4)
	(predicate0 object0 object6)
	(predicate0 object0 object8)
	(predicate0 object0 object10)
	(predicate0 object0 object12)
	(predicate0 object2 object4)
	(predicate0 object2 object6)
	(predicate0 object2 object8)
	(predicate0 object2 object10)
	(predicate0 object2 object12)
	(predicate0 object4 object6)
	(predicate0 object4 object8)
	(predicate0 object4 object10)
	(predicate0 object4 object12)
	(predicate0 object6 object8)
	(predicate0 object6 object10)
	(predicate0 object6 object12)
	(predicate0 object8 object10)
	(predicate0 object8 object12)
	(predicate0 object10 object12)
	(predicate0 object1 object3)
	(predicate0 object1 object5)
	(predicate0 object1 object7)
	(predicate0 object1 object9)
	(predicate0 object1 object11)
	(predicate0 object1 object13)
	(predicate0 object3 object5)
	(predicate0 object3 object7)
	(predicate0 object3 object9)
	(predicate0 object3 object11)
	(predicate0 object3 object13)
	(predicate0 object5 object7)
	(predicate0 object5 object9)
	(predicate0 object5 object11)
	(predicate0 object5 object13)
	(predicate0 object7 object9)
	(predicate0 object7 object11)
	(predicate0 object7 object13)
	(predicate0 object9 object11)
	(predicate0 object9 object13)
	(predicate0 object11 object13)

	(predicate7 object14 object6)
	(predicate4 object14 object2)
	(predicate7 object15 object11)
	(predicate4 object15 object7)

	(predicate6 object8)
	(predicate6 object9)
)

(:goal (and
	(predicate8 object14)
	(predicate8 object15)
))
)

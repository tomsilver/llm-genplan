(define (problem my-problem-3)
	(:domain my-pddl-domain)
	(:objects
		object0 - type0
		object2 - type0
		object4 - type0
		object6 - type0
		object8 - type0
		object10 - type2
		object12 - type2
		object14 - type2
		object16 - type2
		object18 - type2
		object1 - type0
		object3 - type0
		object5 - type0
		object7 - type0
		object9 - type0
		object11 - type2
		object13 - type2
		object15 - type2
		object17 - type2
		object19 - type2
	)

(:init
	(predicate0 object0 object2)
	(predicate0 object0 object4)
	(predicate0 object0 object6)
	(predicate0 object0 object8)
	(predicate0 object2 object4)
	(predicate0 object2 object6)
	(predicate0 object2 object8)
	(predicate0 object4 object6)
	(predicate0 object4 object8)
	(predicate0 object6 object8)
	(predicate0 object1 object3)
	(predicate0 object1 object5)
	(predicate0 object1 object7)
	(predicate0 object1 object9)
	(predicate0 object3 object5)
	(predicate0 object3 object7)
	(predicate0 object3 object9)
	(predicate0 object5 object7)
	(predicate0 object5 object9)
	(predicate0 object7 object9)

	(predicate7 object10 object4)
	(predicate4 object10 object0)
	(predicate7 object12 object8)
	(predicate4 object12 object0)
	(predicate7 object14 object0)
	(predicate4 object14 object6)
	(predicate7 object16 object6)
	(predicate4 object16 object2)
	(predicate7 object18 object2)
	(predicate4 object18 object6)
	(predicate7 object11 object9)
	(predicate4 object11 object1)
	(predicate7 object13 object5)
	(predicate4 object13 object7)
	(predicate7 object15 object3)
	(predicate4 object15 object5)
	(predicate7 object17 object1)
	(predicate4 object17 object5)
	(predicate7 object19 object7)
	(predicate4 object19 object9)

	(predicate6 object2)
	(predicate6 object1)
)

(:goal (and
	(predicate8 object10)
	(predicate8 object12)
	(predicate8 object14)
	(predicate8 object16)
	(predicate8 object18)
	(predicate8 object11)
	(predicate8 object13)
	(predicate8 object15)
	(predicate8 object17)
	(predicate8 object19)
))
)

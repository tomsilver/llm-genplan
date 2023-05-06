(define (problem my-problem-6)
	(:domain my-pddl-domain)
	(:objects
		object3
		object4
		object7
		object8
		object9
		object10
		object11
		object12
		object13
		object14
		object5
		object6
		object0
		object1
		object2
	)

(:init
	(predicate6 object3)
	(predicate6 object4)
	(predicate6 object7)
	(predicate6 object8)
	(predicate6 object9)
	(predicate6 object10)
	(predicate6 object11)
	(predicate6 object12)
	(predicate6 object13)
	(predicate6 object14)
	(predicate6 object5)
	(predicate6 object6)
	(predicate3 object0)
	(predicate3 object1)
	(predicate3 object2)
	(predicate7 object3 object4)
	(predicate7 object3 object7)
	(predicate7 object3 object8)
	(predicate7 object3 object9)
	(predicate7 object3 object10)
	(predicate7 object3 object11)
	(predicate7 object3 object12)
	(predicate7 object3 object13)
	(predicate7 object3 object14)
	(predicate7 object3 object5)
	(predicate7 object3 object6)
	(predicate7 object4 object3)
	(predicate7 object4 object7)
	(predicate7 object4 object8)
	(predicate7 object4 object9)
	(predicate7 object4 object10)
	(predicate7 object4 object11)
	(predicate7 object4 object12)
	(predicate7 object4 object13)
	(predicate7 object4 object14)
	(predicate7 object4 object5)
	(predicate7 object4 object6)
	(predicate7 object7 object3)
	(predicate7 object7 object4)
	(predicate7 object7 object8)
	(predicate7 object7 object9)
	(predicate7 object7 object10)
	(predicate7 object7 object11)
	(predicate7 object7 object12)
	(predicate7 object7 object13)
	(predicate7 object7 object14)
	(predicate7 object7 object5)
	(predicate7 object7 object6)
	(predicate7 object8 object3)
	(predicate7 object8 object4)
	(predicate7 object8 object7)
	(predicate7 object8 object9)
	(predicate7 object8 object10)
	(predicate7 object8 object11)
	(predicate7 object8 object12)
	(predicate7 object8 object13)
	(predicate7 object8 object14)
	(predicate7 object8 object5)
	(predicate7 object8 object6)
	(predicate7 object9 object3)
	(predicate7 object9 object4)
	(predicate7 object9 object7)
	(predicate7 object9 object8)
	(predicate7 object9 object10)
	(predicate7 object9 object11)
	(predicate7 object9 object12)
	(predicate7 object9 object13)
	(predicate7 object9 object14)
	(predicate7 object9 object5)
	(predicate7 object9 object6)
	(predicate7 object10 object3)
	(predicate7 object10 object4)
	(predicate7 object10 object7)
	(predicate7 object10 object8)
	(predicate7 object10 object9)
	(predicate7 object10 object11)
	(predicate7 object10 object12)
	(predicate7 object10 object13)
	(predicate7 object10 object14)
	(predicate7 object10 object5)
	(predicate7 object10 object6)
	(predicate7 object11 object3)
	(predicate7 object11 object4)
	(predicate7 object11 object7)
	(predicate7 object11 object8)
	(predicate7 object11 object9)
	(predicate7 object11 object10)
	(predicate7 object11 object12)
	(predicate7 object11 object13)
	(predicate7 object11 object14)
	(predicate7 object11 object5)
	(predicate7 object11 object6)
	(predicate7 object12 object3)
	(predicate7 object12 object4)
	(predicate7 object12 object7)
	(predicate7 object12 object8)
	(predicate7 object12 object9)
	(predicate7 object12 object10)
	(predicate7 object12 object11)
	(predicate7 object12 object13)
	(predicate7 object12 object14)
	(predicate7 object12 object5)
	(predicate7 object12 object6)
	(predicate7 object13 object3)
	(predicate7 object13 object4)
	(predicate7 object13 object7)
	(predicate7 object13 object8)
	(predicate7 object13 object9)
	(predicate7 object13 object10)
	(predicate7 object13 object11)
	(predicate7 object13 object12)
	(predicate7 object13 object14)
	(predicate7 object13 object5)
	(predicate7 object13 object6)
	(predicate7 object14 object3)
	(predicate7 object14 object4)
	(predicate7 object14 object7)
	(predicate7 object14 object8)
	(predicate7 object14 object9)
	(predicate7 object14 object10)
	(predicate7 object14 object11)
	(predicate7 object14 object12)
	(predicate7 object14 object13)
	(predicate7 object14 object5)
	(predicate7 object14 object6)
	(predicate7 object5 object3)
	(predicate7 object5 object4)
	(predicate7 object5 object7)
	(predicate7 object5 object8)
	(predicate7 object5 object9)
	(predicate7 object5 object10)
	(predicate7 object5 object11)
	(predicate7 object5 object12)
	(predicate7 object5 object13)
	(predicate7 object5 object14)
	(predicate7 object5 object6)
	(predicate7 object6 object3)
	(predicate7 object6 object4)
	(predicate7 object6 object7)
	(predicate7 object6 object8)
	(predicate7 object6 object9)
	(predicate7 object6 object10)
	(predicate7 object6 object11)
	(predicate7 object6 object12)
	(predicate7 object6 object13)
	(predicate7 object6 object14)
	(predicate7 object6 object5)
	(predicate5)
	(predicate0 object0 object12)
	(predicate0 object1 object5)
	(predicate0 object2 object13)
	(predicate1 object4)
)

(:goal (and
	(predicate0 object0 object7)
	(predicate0 object1 object13)
	(predicate0 object2 object11)
)))
(define (problem my-problem-22)
	(:domain my-pddl-domain)
	(:objects
		object0 - type0
		object3 - type0
		object6 - type0
		object9 - type0
		object12 - type0
		object15 - type0
		object18 - type0
		object21 - type0
		object24 - type0
		object27 - type0
		object30 - type2
		object33 - type2
		object36 - type2
		object1 - type0
		object4 - type0
		object7 - type0
		object10 - type0
		object13 - type0
		object16 - type0
		object19 - type0
		object22 - type0
		object25 - type0
		object28 - type0
		object31 - type2
		object34 - type2
		object37 - type2
		object2 - type0
		object5 - type0
		object8 - type0
		object11 - type0
		object14 - type0
		object17 - type0
		object20 - type0
		object23 - type0
		object26 - type0
		object29 - type0
		object32 - type2
		object35 - type2
		object38 - type2
	)

(:init
	(predicate0 object0 object3)
	(predicate0 object0 object6)
	(predicate0 object0 object9)
	(predicate0 object0 object12)
	(predicate0 object0 object15)
	(predicate0 object0 object18)
	(predicate0 object0 object21)
	(predicate0 object0 object24)
	(predicate0 object0 object27)
	(predicate0 object3 object6)
	(predicate0 object3 object9)
	(predicate0 object3 object12)
	(predicate0 object3 object15)
	(predicate0 object3 object18)
	(predicate0 object3 object21)
	(predicate0 object3 object24)
	(predicate0 object3 object27)
	(predicate0 object6 object9)
	(predicate0 object6 object12)
	(predicate0 object6 object15)
	(predicate0 object6 object18)
	(predicate0 object6 object21)
	(predicate0 object6 object24)
	(predicate0 object6 object27)
	(predicate0 object9 object12)
	(predicate0 object9 object15)
	(predicate0 object9 object18)
	(predicate0 object9 object21)
	(predicate0 object9 object24)
	(predicate0 object9 object27)
	(predicate0 object12 object15)
	(predicate0 object12 object18)
	(predicate0 object12 object21)
	(predicate0 object12 object24)
	(predicate0 object12 object27)
	(predicate0 object15 object18)
	(predicate0 object15 object21)
	(predicate0 object15 object24)
	(predicate0 object15 object27)
	(predicate0 object18 object21)
	(predicate0 object18 object24)
	(predicate0 object18 object27)
	(predicate0 object21 object24)
	(predicate0 object21 object27)
	(predicate0 object24 object27)
	(predicate0 object1 object4)
	(predicate0 object1 object7)
	(predicate0 object1 object10)
	(predicate0 object1 object13)
	(predicate0 object1 object16)
	(predicate0 object1 object19)
	(predicate0 object1 object22)
	(predicate0 object1 object25)
	(predicate0 object1 object28)
	(predicate0 object4 object7)
	(predicate0 object4 object10)
	(predicate0 object4 object13)
	(predicate0 object4 object16)
	(predicate0 object4 object19)
	(predicate0 object4 object22)
	(predicate0 object4 object25)
	(predicate0 object4 object28)
	(predicate0 object7 object10)
	(predicate0 object7 object13)
	(predicate0 object7 object16)
	(predicate0 object7 object19)
	(predicate0 object7 object22)
	(predicate0 object7 object25)
	(predicate0 object7 object28)
	(predicate0 object10 object13)
	(predicate0 object10 object16)
	(predicate0 object10 object19)
	(predicate0 object10 object22)
	(predicate0 object10 object25)
	(predicate0 object10 object28)
	(predicate0 object13 object16)
	(predicate0 object13 object19)
	(predicate0 object13 object22)
	(predicate0 object13 object25)
	(predicate0 object13 object28)
	(predicate0 object16 object19)
	(predicate0 object16 object22)
	(predicate0 object16 object25)
	(predicate0 object16 object28)
	(predicate0 object19 object22)
	(predicate0 object19 object25)
	(predicate0 object19 object28)
	(predicate0 object22 object25)
	(predicate0 object22 object28)
	(predicate0 object25 object28)
	(predicate0 object2 object5)
	(predicate0 object2 object8)
	(predicate0 object2 object11)
	(predicate0 object2 object14)
	(predicate0 object2 object17)
	(predicate0 object2 object20)
	(predicate0 object2 object23)
	(predicate0 object2 object26)
	(predicate0 object2 object29)
	(predicate0 object5 object8)
	(predicate0 object5 object11)
	(predicate0 object5 object14)
	(predicate0 object5 object17)
	(predicate0 object5 object20)
	(predicate0 object5 object23)
	(predicate0 object5 object26)
	(predicate0 object5 object29)
	(predicate0 object8 object11)
	(predicate0 object8 object14)
	(predicate0 object8 object17)
	(predicate0 object8 object20)
	(predicate0 object8 object23)
	(predicate0 object8 object26)
	(predicate0 object8 object29)
	(predicate0 object11 object14)
	(predicate0 object11 object17)
	(predicate0 object11 object20)
	(predicate0 object11 object23)
	(predicate0 object11 object26)
	(predicate0 object11 object29)
	(predicate0 object14 object17)
	(predicate0 object14 object20)
	(predicate0 object14 object23)
	(predicate0 object14 object26)
	(predicate0 object14 object29)
	(predicate0 object17 object20)
	(predicate0 object17 object23)
	(predicate0 object17 object26)
	(predicate0 object17 object29)
	(predicate0 object20 object23)
	(predicate0 object20 object26)
	(predicate0 object20 object29)
	(predicate0 object23 object26)
	(predicate0 object23 object29)
	(predicate0 object26 object29)

	(predicate7 object30 object0)
	(predicate4 object30 object24)
	(predicate7 object33 object3)
	(predicate4 object33 object0)
	(predicate7 object36 object15)
	(predicate4 object36 object0)
	(predicate7 object31 object1)
	(predicate4 object31 object13)
	(predicate7 object34 object19)
	(predicate4 object34 object4)
	(predicate7 object37 object4)
	(predicate4 object37 object19)
	(predicate7 object32 object20)
	(predicate4 object32 object8)
	(predicate7 object35 object11)
	(predicate4 object35 object26)
	(predicate7 object38 object26)
	(predicate4 object38 object8)

	(predicate6 object15)
	(predicate6 object13)
	(predicate6 object8)
)

(:goal (and
	(predicate8 object30)
	(predicate8 object33)
	(predicate8 object36)
	(predicate8 object31)
	(predicate8 object34)
	(predicate8 object37)
	(predicate8 object32)
	(predicate8 object35)
	(predicate8 object38)
))
)

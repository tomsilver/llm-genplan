(define (problem my-problem-13)
	(:domain my-pddl-domain)
	(:objects
		object11
		object12
		object23
		object24
		object25
		object26
		object27
		object28
		object29
		object30
		object13
		object14
		object15
		object16
		object17
		object18
		object19
		object20
		object21
		object22
		object0
		object1
		object3
		object4
		object5
		object6
		object7
		object8
		object9
		object10
		object2
	)

(:init
	(predicate6 object11)
	(predicate6 object12)
	(predicate6 object23)
	(predicate6 object24)
	(predicate6 object25)
	(predicate6 object26)
	(predicate6 object27)
	(predicate6 object28)
	(predicate6 object29)
	(predicate6 object30)
	(predicate6 object13)
	(predicate6 object14)
	(predicate6 object15)
	(predicate6 object16)
	(predicate6 object17)
	(predicate6 object18)
	(predicate6 object19)
	(predicate6 object20)
	(predicate6 object21)
	(predicate6 object22)
	(predicate3 object0)
	(predicate3 object1)
	(predicate3 object3)
	(predicate3 object4)
	(predicate3 object5)
	(predicate3 object6)
	(predicate3 object7)
	(predicate3 object8)
	(predicate3 object9)
	(predicate3 object10)
	(predicate3 object2)
	(predicate7 object11 object12)
	(predicate7 object11 object23)
	(predicate7 object11 object24)
	(predicate7 object11 object25)
	(predicate7 object11 object26)
	(predicate7 object11 object27)
	(predicate7 object11 object28)
	(predicate7 object11 object29)
	(predicate7 object11 object30)
	(predicate7 object11 object13)
	(predicate7 object11 object14)
	(predicate7 object11 object15)
	(predicate7 object11 object16)
	(predicate7 object11 object17)
	(predicate7 object11 object18)
	(predicate7 object11 object19)
	(predicate7 object11 object20)
	(predicate7 object11 object21)
	(predicate7 object11 object22)
	(predicate7 object12 object11)
	(predicate7 object12 object23)
	(predicate7 object12 object24)
	(predicate7 object12 object25)
	(predicate7 object12 object26)
	(predicate7 object12 object27)
	(predicate7 object12 object28)
	(predicate7 object12 object29)
	(predicate7 object12 object30)
	(predicate7 object12 object13)
	(predicate7 object12 object14)
	(predicate7 object12 object15)
	(predicate7 object12 object16)
	(predicate7 object12 object17)
	(predicate7 object12 object18)
	(predicate7 object12 object19)
	(predicate7 object12 object20)
	(predicate7 object12 object21)
	(predicate7 object12 object22)
	(predicate7 object23 object11)
	(predicate7 object23 object12)
	(predicate7 object23 object24)
	(predicate7 object23 object25)
	(predicate7 object23 object26)
	(predicate7 object23 object27)
	(predicate7 object23 object28)
	(predicate7 object23 object29)
	(predicate7 object23 object30)
	(predicate7 object23 object13)
	(predicate7 object23 object14)
	(predicate7 object23 object15)
	(predicate7 object23 object16)
	(predicate7 object23 object17)
	(predicate7 object23 object18)
	(predicate7 object23 object19)
	(predicate7 object23 object20)
	(predicate7 object23 object21)
	(predicate7 object23 object22)
	(predicate7 object24 object11)
	(predicate7 object24 object12)
	(predicate7 object24 object23)
	(predicate7 object24 object25)
	(predicate7 object24 object26)
	(predicate7 object24 object27)
	(predicate7 object24 object28)
	(predicate7 object24 object29)
	(predicate7 object24 object30)
	(predicate7 object24 object13)
	(predicate7 object24 object14)
	(predicate7 object24 object15)
	(predicate7 object24 object16)
	(predicate7 object24 object17)
	(predicate7 object24 object18)
	(predicate7 object24 object19)
	(predicate7 object24 object20)
	(predicate7 object24 object21)
	(predicate7 object24 object22)
	(predicate7 object25 object11)
	(predicate7 object25 object12)
	(predicate7 object25 object23)
	(predicate7 object25 object24)
	(predicate7 object25 object26)
	(predicate7 object25 object27)
	(predicate7 object25 object28)
	(predicate7 object25 object29)
	(predicate7 object25 object30)
	(predicate7 object25 object13)
	(predicate7 object25 object14)
	(predicate7 object25 object15)
	(predicate7 object25 object16)
	(predicate7 object25 object17)
	(predicate7 object25 object18)
	(predicate7 object25 object19)
	(predicate7 object25 object20)
	(predicate7 object25 object21)
	(predicate7 object25 object22)
	(predicate7 object26 object11)
	(predicate7 object26 object12)
	(predicate7 object26 object23)
	(predicate7 object26 object24)
	(predicate7 object26 object25)
	(predicate7 object26 object27)
	(predicate7 object26 object28)
	(predicate7 object26 object29)
	(predicate7 object26 object30)
	(predicate7 object26 object13)
	(predicate7 object26 object14)
	(predicate7 object26 object15)
	(predicate7 object26 object16)
	(predicate7 object26 object17)
	(predicate7 object26 object18)
	(predicate7 object26 object19)
	(predicate7 object26 object20)
	(predicate7 object26 object21)
	(predicate7 object26 object22)
	(predicate7 object27 object11)
	(predicate7 object27 object12)
	(predicate7 object27 object23)
	(predicate7 object27 object24)
	(predicate7 object27 object25)
	(predicate7 object27 object26)
	(predicate7 object27 object28)
	(predicate7 object27 object29)
	(predicate7 object27 object30)
	(predicate7 object27 object13)
	(predicate7 object27 object14)
	(predicate7 object27 object15)
	(predicate7 object27 object16)
	(predicate7 object27 object17)
	(predicate7 object27 object18)
	(predicate7 object27 object19)
	(predicate7 object27 object20)
	(predicate7 object27 object21)
	(predicate7 object27 object22)
	(predicate7 object28 object11)
	(predicate7 object28 object12)
	(predicate7 object28 object23)
	(predicate7 object28 object24)
	(predicate7 object28 object25)
	(predicate7 object28 object26)
	(predicate7 object28 object27)
	(predicate7 object28 object29)
	(predicate7 object28 object30)
	(predicate7 object28 object13)
	(predicate7 object28 object14)
	(predicate7 object28 object15)
	(predicate7 object28 object16)
	(predicate7 object28 object17)
	(predicate7 object28 object18)
	(predicate7 object28 object19)
	(predicate7 object28 object20)
	(predicate7 object28 object21)
	(predicate7 object28 object22)
	(predicate7 object29 object11)
	(predicate7 object29 object12)
	(predicate7 object29 object23)
	(predicate7 object29 object24)
	(predicate7 object29 object25)
	(predicate7 object29 object26)
	(predicate7 object29 object27)
	(predicate7 object29 object28)
	(predicate7 object29 object30)
	(predicate7 object29 object13)
	(predicate7 object29 object14)
	(predicate7 object29 object15)
	(predicate7 object29 object16)
	(predicate7 object29 object17)
	(predicate7 object29 object18)
	(predicate7 object29 object19)
	(predicate7 object29 object20)
	(predicate7 object29 object21)
	(predicate7 object29 object22)
	(predicate7 object30 object11)
	(predicate7 object30 object12)
	(predicate7 object30 object23)
	(predicate7 object30 object24)
	(predicate7 object30 object25)
	(predicate7 object30 object26)
	(predicate7 object30 object27)
	(predicate7 object30 object28)
	(predicate7 object30 object29)
	(predicate7 object30 object13)
	(predicate7 object30 object14)
	(predicate7 object30 object15)
	(predicate7 object30 object16)
	(predicate7 object30 object17)
	(predicate7 object30 object18)
	(predicate7 object30 object19)
	(predicate7 object30 object20)
	(predicate7 object30 object21)
	(predicate7 object30 object22)
	(predicate7 object13 object11)
	(predicate7 object13 object12)
	(predicate7 object13 object23)
	(predicate7 object13 object24)
	(predicate7 object13 object25)
	(predicate7 object13 object26)
	(predicate7 object13 object27)
	(predicate7 object13 object28)
	(predicate7 object13 object29)
	(predicate7 object13 object30)
	(predicate7 object13 object14)
	(predicate7 object13 object15)
	(predicate7 object13 object16)
	(predicate7 object13 object17)
	(predicate7 object13 object18)
	(predicate7 object13 object19)
	(predicate7 object13 object20)
	(predicate7 object13 object21)
	(predicate7 object13 object22)
	(predicate7 object14 object11)
	(predicate7 object14 object12)
	(predicate7 object14 object23)
	(predicate7 object14 object24)
	(predicate7 object14 object25)
	(predicate7 object14 object26)
	(predicate7 object14 object27)
	(predicate7 object14 object28)
	(predicate7 object14 object29)
	(predicate7 object14 object30)
	(predicate7 object14 object13)
	(predicate7 object14 object15)
	(predicate7 object14 object16)
	(predicate7 object14 object17)
	(predicate7 object14 object18)
	(predicate7 object14 object19)
	(predicate7 object14 object20)
	(predicate7 object14 object21)
	(predicate7 object14 object22)
	(predicate7 object15 object11)
	(predicate7 object15 object12)
	(predicate7 object15 object23)
	(predicate7 object15 object24)
	(predicate7 object15 object25)
	(predicate7 object15 object26)
	(predicate7 object15 object27)
	(predicate7 object15 object28)
	(predicate7 object15 object29)
	(predicate7 object15 object30)
	(predicate7 object15 object13)
	(predicate7 object15 object14)
	(predicate7 object15 object16)
	(predicate7 object15 object17)
	(predicate7 object15 object18)
	(predicate7 object15 object19)
	(predicate7 object15 object20)
	(predicate7 object15 object21)
	(predicate7 object15 object22)
	(predicate7 object16 object11)
	(predicate7 object16 object12)
	(predicate7 object16 object23)
	(predicate7 object16 object24)
	(predicate7 object16 object25)
	(predicate7 object16 object26)
	(predicate7 object16 object27)
	(predicate7 object16 object28)
	(predicate7 object16 object29)
	(predicate7 object16 object30)
	(predicate7 object16 object13)
	(predicate7 object16 object14)
	(predicate7 object16 object15)
	(predicate7 object16 object17)
	(predicate7 object16 object18)
	(predicate7 object16 object19)
	(predicate7 object16 object20)
	(predicate7 object16 object21)
	(predicate7 object16 object22)
	(predicate7 object17 object11)
	(predicate7 object17 object12)
	(predicate7 object17 object23)
	(predicate7 object17 object24)
	(predicate7 object17 object25)
	(predicate7 object17 object26)
	(predicate7 object17 object27)
	(predicate7 object17 object28)
	(predicate7 object17 object29)
	(predicate7 object17 object30)
	(predicate7 object17 object13)
	(predicate7 object17 object14)
	(predicate7 object17 object15)
	(predicate7 object17 object16)
	(predicate7 object17 object18)
	(predicate7 object17 object19)
	(predicate7 object17 object20)
	(predicate7 object17 object21)
	(predicate7 object17 object22)
	(predicate7 object18 object11)
	(predicate7 object18 object12)
	(predicate7 object18 object23)
	(predicate7 object18 object24)
	(predicate7 object18 object25)
	(predicate7 object18 object26)
	(predicate7 object18 object27)
	(predicate7 object18 object28)
	(predicate7 object18 object29)
	(predicate7 object18 object30)
	(predicate7 object18 object13)
	(predicate7 object18 object14)
	(predicate7 object18 object15)
	(predicate7 object18 object16)
	(predicate7 object18 object17)
	(predicate7 object18 object19)
	(predicate7 object18 object20)
	(predicate7 object18 object21)
	(predicate7 object18 object22)
	(predicate7 object19 object11)
	(predicate7 object19 object12)
	(predicate7 object19 object23)
	(predicate7 object19 object24)
	(predicate7 object19 object25)
	(predicate7 object19 object26)
	(predicate7 object19 object27)
	(predicate7 object19 object28)
	(predicate7 object19 object29)
	(predicate7 object19 object30)
	(predicate7 object19 object13)
	(predicate7 object19 object14)
	(predicate7 object19 object15)
	(predicate7 object19 object16)
	(predicate7 object19 object17)
	(predicate7 object19 object18)
	(predicate7 object19 object20)
	(predicate7 object19 object21)
	(predicate7 object19 object22)
	(predicate7 object20 object11)
	(predicate7 object20 object12)
	(predicate7 object20 object23)
	(predicate7 object20 object24)
	(predicate7 object20 object25)
	(predicate7 object20 object26)
	(predicate7 object20 object27)
	(predicate7 object20 object28)
	(predicate7 object20 object29)
	(predicate7 object20 object30)
	(predicate7 object20 object13)
	(predicate7 object20 object14)
	(predicate7 object20 object15)
	(predicate7 object20 object16)
	(predicate7 object20 object17)
	(predicate7 object20 object18)
	(predicate7 object20 object19)
	(predicate7 object20 object21)
	(predicate7 object20 object22)
	(predicate7 object21 object11)
	(predicate7 object21 object12)
	(predicate7 object21 object23)
	(predicate7 object21 object24)
	(predicate7 object21 object25)
	(predicate7 object21 object26)
	(predicate7 object21 object27)
	(predicate7 object21 object28)
	(predicate7 object21 object29)
	(predicate7 object21 object30)
	(predicate7 object21 object13)
	(predicate7 object21 object14)
	(predicate7 object21 object15)
	(predicate7 object21 object16)
	(predicate7 object21 object17)
	(predicate7 object21 object18)
	(predicate7 object21 object19)
	(predicate7 object21 object20)
	(predicate7 object21 object22)
	(predicate7 object22 object11)
	(predicate7 object22 object12)
	(predicate7 object22 object23)
	(predicate7 object22 object24)
	(predicate7 object22 object25)
	(predicate7 object22 object26)
	(predicate7 object22 object27)
	(predicate7 object22 object28)
	(predicate7 object22 object29)
	(predicate7 object22 object30)
	(predicate7 object22 object13)
	(predicate7 object22 object14)
	(predicate7 object22 object15)
	(predicate7 object22 object16)
	(predicate7 object22 object17)
	(predicate7 object22 object18)
	(predicate7 object22 object19)
	(predicate7 object22 object20)
	(predicate7 object22 object21)
	(predicate5)
	(predicate0 object0 object28)
	(predicate0 object1 object29)
	(predicate0 object3 object23)
	(predicate0 object4 object23)
	(predicate0 object5 object11)
	(predicate0 object6 object13)
	(predicate0 object7 object16)
	(predicate0 object8 object23)
	(predicate0 object9 object15)
	(predicate0 object10 object18)
	(predicate0 object2 object12)
	(predicate1 object24)
)

(:goal (and
	(predicate0 object0 object24)
	(predicate0 object1 object28)
	(predicate0 object3 object22)
	(predicate0 object4 object24)
	(predicate0 object5 object25)
	(predicate0 object6 object30)
	(predicate0 object7 object17)
	(predicate0 object8 object25)
	(predicate0 object9 object26)
	(predicate0 object10 object22)
	(predicate0 object2 object26)
)))
(define (problem my-problem-28)
	(:domain my-pddl-domain)
	(:objects
		object0 - type0
		object6 - type0
		object9 - type0
		object12 - type0
		object15 - type0
		object18 - type0
		object21 - type0
		object24 - type0
		object27 - type0
		object30 - type0
		object3 - type0
		object33 - type2
		object36 - type2
		object39 - type2
		object42 - type2
		object45 - type2
		object48 - type2
		object51 - type2
		object54 - type2
		object57 - type2
		object60 - type2
		object1 - type0
		object7 - type0
		object10 - type0
		object13 - type0
		object16 - type0
		object19 - type0
		object22 - type0
		object25 - type0
		object28 - type0
		object31 - type0
		object4 - type0
		object34 - type2
		object37 - type2
		object40 - type2
		object43 - type2
		object46 - type2
		object49 - type2
		object52 - type2
		object55 - type2
		object58 - type2
		object61 - type2
		object2 - type0
		object8 - type0
		object11 - type0
		object14 - type0
		object17 - type0
		object20 - type0
		object23 - type0
		object26 - type0
		object29 - type0
		object32 - type0
		object5 - type0
		object35 - type2
		object38 - type2
		object41 - type2
		object44 - type2
		object47 - type2
		object50 - type2
		object53 - type2
		object56 - type2
		object59 - type2
		object62 - type2
	)

(:init
	(predicate0 object0 object6)
	(predicate0 object0 object9)
	(predicate0 object0 object12)
	(predicate0 object0 object15)
	(predicate0 object0 object18)
	(predicate0 object0 object21)
	(predicate0 object0 object24)
	(predicate0 object0 object27)
	(predicate0 object0 object30)
	(predicate0 object0 object3)
	(predicate0 object6 object9)
	(predicate0 object6 object12)
	(predicate0 object6 object15)
	(predicate0 object6 object18)
	(predicate0 object6 object21)
	(predicate0 object6 object24)
	(predicate0 object6 object27)
	(predicate0 object6 object30)
	(predicate0 object6 object3)
	(predicate0 object9 object12)
	(predicate0 object9 object15)
	(predicate0 object9 object18)
	(predicate0 object9 object21)
	(predicate0 object9 object24)
	(predicate0 object9 object27)
	(predicate0 object9 object30)
	(predicate0 object9 object3)
	(predicate0 object12 object15)
	(predicate0 object12 object18)
	(predicate0 object12 object21)
	(predicate0 object12 object24)
	(predicate0 object12 object27)
	(predicate0 object12 object30)
	(predicate0 object12 object3)
	(predicate0 object15 object18)
	(predicate0 object15 object21)
	(predicate0 object15 object24)
	(predicate0 object15 object27)
	(predicate0 object15 object30)
	(predicate0 object15 object3)
	(predicate0 object18 object21)
	(predicate0 object18 object24)
	(predicate0 object18 object27)
	(predicate0 object18 object30)
	(predicate0 object18 object3)
	(predicate0 object21 object24)
	(predicate0 object21 object27)
	(predicate0 object21 object30)
	(predicate0 object21 object3)
	(predicate0 object24 object27)
	(predicate0 object24 object30)
	(predicate0 object24 object3)
	(predicate0 object27 object30)
	(predicate0 object27 object3)
	(predicate0 object30 object3)
	(predicate0 object1 object7)
	(predicate0 object1 object10)
	(predicate0 object1 object13)
	(predicate0 object1 object16)
	(predicate0 object1 object19)
	(predicate0 object1 object22)
	(predicate0 object1 object25)
	(predicate0 object1 object28)
	(predicate0 object1 object31)
	(predicate0 object1 object4)
	(predicate0 object7 object10)
	(predicate0 object7 object13)
	(predicate0 object7 object16)
	(predicate0 object7 object19)
	(predicate0 object7 object22)
	(predicate0 object7 object25)
	(predicate0 object7 object28)
	(predicate0 object7 object31)
	(predicate0 object7 object4)
	(predicate0 object10 object13)
	(predicate0 object10 object16)
	(predicate0 object10 object19)
	(predicate0 object10 object22)
	(predicate0 object10 object25)
	(predicate0 object10 object28)
	(predicate0 object10 object31)
	(predicate0 object10 object4)
	(predicate0 object13 object16)
	(predicate0 object13 object19)
	(predicate0 object13 object22)
	(predicate0 object13 object25)
	(predicate0 object13 object28)
	(predicate0 object13 object31)
	(predicate0 object13 object4)
	(predicate0 object16 object19)
	(predicate0 object16 object22)
	(predicate0 object16 object25)
	(predicate0 object16 object28)
	(predicate0 object16 object31)
	(predicate0 object16 object4)
	(predicate0 object19 object22)
	(predicate0 object19 object25)
	(predicate0 object19 object28)
	(predicate0 object19 object31)
	(predicate0 object19 object4)
	(predicate0 object22 object25)
	(predicate0 object22 object28)
	(predicate0 object22 object31)
	(predicate0 object22 object4)
	(predicate0 object25 object28)
	(predicate0 object25 object31)
	(predicate0 object25 object4)
	(predicate0 object28 object31)
	(predicate0 object28 object4)
	(predicate0 object31 object4)
	(predicate0 object2 object8)
	(predicate0 object2 object11)
	(predicate0 object2 object14)
	(predicate0 object2 object17)
	(predicate0 object2 object20)
	(predicate0 object2 object23)
	(predicate0 object2 object26)
	(predicate0 object2 object29)
	(predicate0 object2 object32)
	(predicate0 object2 object5)
	(predicate0 object8 object11)
	(predicate0 object8 object14)
	(predicate0 object8 object17)
	(predicate0 object8 object20)
	(predicate0 object8 object23)
	(predicate0 object8 object26)
	(predicate0 object8 object29)
	(predicate0 object8 object32)
	(predicate0 object8 object5)
	(predicate0 object11 object14)
	(predicate0 object11 object17)
	(predicate0 object11 object20)
	(predicate0 object11 object23)
	(predicate0 object11 object26)
	(predicate0 object11 object29)
	(predicate0 object11 object32)
	(predicate0 object11 object5)
	(predicate0 object14 object17)
	(predicate0 object14 object20)
	(predicate0 object14 object23)
	(predicate0 object14 object26)
	(predicate0 object14 object29)
	(predicate0 object14 object32)
	(predicate0 object14 object5)
	(predicate0 object17 object20)
	(predicate0 object17 object23)
	(predicate0 object17 object26)
	(predicate0 object17 object29)
	(predicate0 object17 object32)
	(predicate0 object17 object5)
	(predicate0 object20 object23)
	(predicate0 object20 object26)
	(predicate0 object20 object29)
	(predicate0 object20 object32)
	(predicate0 object20 object5)
	(predicate0 object23 object26)
	(predicate0 object23 object29)
	(predicate0 object23 object32)
	(predicate0 object23 object5)
	(predicate0 object26 object29)
	(predicate0 object26 object32)
	(predicate0 object26 object5)
	(predicate0 object29 object32)
	(predicate0 object29 object5)
	(predicate0 object32 object5)

	(predicate7 object33 object12)
	(predicate4 object33 object24)
	(predicate7 object36 object18)
	(predicate4 object36 object0)
	(predicate7 object39 object24)
	(predicate4 object39 object9)
	(predicate7 object42 object27)
	(predicate4 object42 object3)
	(predicate7 object45 object9)
	(predicate4 object45 object15)
	(predicate7 object48 object15)
	(predicate4 object48 object6)
	(predicate7 object51 object3)
	(predicate4 object51 object30)
	(predicate7 object54 object0)
	(predicate4 object54 object15)
	(predicate7 object57 object6)
	(predicate4 object57 object0)
	(predicate7 object60 object21)
	(predicate4 object60 object24)
	(predicate7 object34 object7)
	(predicate4 object34 object19)
	(predicate7 object37 object31)
	(predicate4 object37 object7)
	(predicate7 object40 object10)
	(predicate4 object40 object1)
	(predicate7 object43 object1)
	(predicate4 object43 object19)
	(predicate7 object46 object4)
	(predicate4 object46 object19)
	(predicate7 object49 object22)
	(predicate4 object49 object28)
	(predicate7 object52 object16)
	(predicate4 object52 object7)
	(predicate7 object55 object25)
	(predicate4 object55 object7)
	(predicate7 object58 object28)
	(predicate4 object58 object10)
	(predicate7 object61 object13)
	(predicate4 object61 object10)
	(predicate7 object35 object11)
	(predicate4 object35 object23)
	(predicate7 object38 object20)
	(predicate4 object38 object8)
	(predicate7 object41 object5)
	(predicate4 object41 object32)
	(predicate7 object44 object23)
	(predicate4 object44 object11)
	(predicate7 object47 object8)
	(predicate4 object47 object14)
	(predicate7 object50 object29)
	(predicate4 object50 object2)
	(predicate7 object53 object17)
	(predicate4 object53 object5)
	(predicate7 object56 object14)
	(predicate4 object56 object11)
	(predicate7 object59 object26)
	(predicate4 object59 object23)
	(predicate7 object62 object2)
	(predicate4 object62 object8)

	(predicate6 object3)
	(predicate6 object13)
	(predicate6 object17)
)

(:goal (and
	(predicate8 object33)
	(predicate8 object36)
	(predicate8 object39)
	(predicate8 object42)
	(predicate8 object45)
	(predicate8 object48)
	(predicate8 object51)
	(predicate8 object54)
	(predicate8 object57)
	(predicate8 object60)
	(predicate8 object34)
	(predicate8 object37)
	(predicate8 object40)
	(predicate8 object43)
	(predicate8 object46)
	(predicate8 object49)
	(predicate8 object52)
	(predicate8 object55)
	(predicate8 object58)
	(predicate8 object61)
	(predicate8 object35)
	(predicate8 object38)
	(predicate8 object41)
	(predicate8 object44)
	(predicate8 object47)
	(predicate8 object50)
	(predicate8 object53)
	(predicate8 object56)
	(predicate8 object59)
	(predicate8 object62)
))
)

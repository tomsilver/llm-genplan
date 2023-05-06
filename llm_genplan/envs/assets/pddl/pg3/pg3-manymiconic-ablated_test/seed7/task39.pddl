(define (problem my-problem-39)
	(:domain my-pddl-domain)
	(:objects
		object0 - type0
		object5 - type0
		object10 - type0
		object15 - type0
		object20 - type0
		object25 - type0
		object30 - type0
		object35 - type0
		object40 - type0
		object45 - type0
		object50 - type2
		object55 - type2
		object60 - type2
		object65 - type2
		object70 - type2
		object75 - type2
		object80 - type2
		object1 - type0
		object6 - type0
		object11 - type0
		object16 - type0
		object21 - type0
		object26 - type0
		object31 - type0
		object36 - type0
		object41 - type0
		object46 - type0
		object51 - type2
		object56 - type2
		object61 - type2
		object66 - type2
		object71 - type2
		object76 - type2
		object81 - type2
		object2 - type0
		object7 - type0
		object12 - type0
		object17 - type0
		object22 - type0
		object27 - type0
		object32 - type0
		object37 - type0
		object42 - type0
		object47 - type0
		object52 - type2
		object57 - type2
		object62 - type2
		object67 - type2
		object72 - type2
		object77 - type2
		object82 - type2
		object3 - type0
		object8 - type0
		object13 - type0
		object18 - type0
		object23 - type0
		object28 - type0
		object33 - type0
		object38 - type0
		object43 - type0
		object48 - type0
		object53 - type2
		object58 - type2
		object63 - type2
		object68 - type2
		object73 - type2
		object78 - type2
		object83 - type2
		object4 - type0
		object9 - type0
		object14 - type0
		object19 - type0
		object24 - type0
		object29 - type0
		object34 - type0
		object39 - type0
		object44 - type0
		object49 - type0
		object54 - type2
		object59 - type2
		object64 - type2
		object69 - type2
		object74 - type2
		object79 - type2
		object84 - type2
	)

(:init
	(predicate0 object0 object5)
	(predicate0 object0 object10)
	(predicate0 object0 object15)
	(predicate0 object0 object20)
	(predicate0 object0 object25)
	(predicate0 object0 object30)
	(predicate0 object0 object35)
	(predicate0 object0 object40)
	(predicate0 object0 object45)
	(predicate0 object5 object10)
	(predicate0 object5 object15)
	(predicate0 object5 object20)
	(predicate0 object5 object25)
	(predicate0 object5 object30)
	(predicate0 object5 object35)
	(predicate0 object5 object40)
	(predicate0 object5 object45)
	(predicate0 object10 object15)
	(predicate0 object10 object20)
	(predicate0 object10 object25)
	(predicate0 object10 object30)
	(predicate0 object10 object35)
	(predicate0 object10 object40)
	(predicate0 object10 object45)
	(predicate0 object15 object20)
	(predicate0 object15 object25)
	(predicate0 object15 object30)
	(predicate0 object15 object35)
	(predicate0 object15 object40)
	(predicate0 object15 object45)
	(predicate0 object20 object25)
	(predicate0 object20 object30)
	(predicate0 object20 object35)
	(predicate0 object20 object40)
	(predicate0 object20 object45)
	(predicate0 object25 object30)
	(predicate0 object25 object35)
	(predicate0 object25 object40)
	(predicate0 object25 object45)
	(predicate0 object30 object35)
	(predicate0 object30 object40)
	(predicate0 object30 object45)
	(predicate0 object35 object40)
	(predicate0 object35 object45)
	(predicate0 object40 object45)
	(predicate0 object1 object6)
	(predicate0 object1 object11)
	(predicate0 object1 object16)
	(predicate0 object1 object21)
	(predicate0 object1 object26)
	(predicate0 object1 object31)
	(predicate0 object1 object36)
	(predicate0 object1 object41)
	(predicate0 object1 object46)
	(predicate0 object6 object11)
	(predicate0 object6 object16)
	(predicate0 object6 object21)
	(predicate0 object6 object26)
	(predicate0 object6 object31)
	(predicate0 object6 object36)
	(predicate0 object6 object41)
	(predicate0 object6 object46)
	(predicate0 object11 object16)
	(predicate0 object11 object21)
	(predicate0 object11 object26)
	(predicate0 object11 object31)
	(predicate0 object11 object36)
	(predicate0 object11 object41)
	(predicate0 object11 object46)
	(predicate0 object16 object21)
	(predicate0 object16 object26)
	(predicate0 object16 object31)
	(predicate0 object16 object36)
	(predicate0 object16 object41)
	(predicate0 object16 object46)
	(predicate0 object21 object26)
	(predicate0 object21 object31)
	(predicate0 object21 object36)
	(predicate0 object21 object41)
	(predicate0 object21 object46)
	(predicate0 object26 object31)
	(predicate0 object26 object36)
	(predicate0 object26 object41)
	(predicate0 object26 object46)
	(predicate0 object31 object36)
	(predicate0 object31 object41)
	(predicate0 object31 object46)
	(predicate0 object36 object41)
	(predicate0 object36 object46)
	(predicate0 object41 object46)
	(predicate0 object2 object7)
	(predicate0 object2 object12)
	(predicate0 object2 object17)
	(predicate0 object2 object22)
	(predicate0 object2 object27)
	(predicate0 object2 object32)
	(predicate0 object2 object37)
	(predicate0 object2 object42)
	(predicate0 object2 object47)
	(predicate0 object7 object12)
	(predicate0 object7 object17)
	(predicate0 object7 object22)
	(predicate0 object7 object27)
	(predicate0 object7 object32)
	(predicate0 object7 object37)
	(predicate0 object7 object42)
	(predicate0 object7 object47)
	(predicate0 object12 object17)
	(predicate0 object12 object22)
	(predicate0 object12 object27)
	(predicate0 object12 object32)
	(predicate0 object12 object37)
	(predicate0 object12 object42)
	(predicate0 object12 object47)
	(predicate0 object17 object22)
	(predicate0 object17 object27)
	(predicate0 object17 object32)
	(predicate0 object17 object37)
	(predicate0 object17 object42)
	(predicate0 object17 object47)
	(predicate0 object22 object27)
	(predicate0 object22 object32)
	(predicate0 object22 object37)
	(predicate0 object22 object42)
	(predicate0 object22 object47)
	(predicate0 object27 object32)
	(predicate0 object27 object37)
	(predicate0 object27 object42)
	(predicate0 object27 object47)
	(predicate0 object32 object37)
	(predicate0 object32 object42)
	(predicate0 object32 object47)
	(predicate0 object37 object42)
	(predicate0 object37 object47)
	(predicate0 object42 object47)
	(predicate0 object3 object8)
	(predicate0 object3 object13)
	(predicate0 object3 object18)
	(predicate0 object3 object23)
	(predicate0 object3 object28)
	(predicate0 object3 object33)
	(predicate0 object3 object38)
	(predicate0 object3 object43)
	(predicate0 object3 object48)
	(predicate0 object8 object13)
	(predicate0 object8 object18)
	(predicate0 object8 object23)
	(predicate0 object8 object28)
	(predicate0 object8 object33)
	(predicate0 object8 object38)
	(predicate0 object8 object43)
	(predicate0 object8 object48)
	(predicate0 object13 object18)
	(predicate0 object13 object23)
	(predicate0 object13 object28)
	(predicate0 object13 object33)
	(predicate0 object13 object38)
	(predicate0 object13 object43)
	(predicate0 object13 object48)
	(predicate0 object18 object23)
	(predicate0 object18 object28)
	(predicate0 object18 object33)
	(predicate0 object18 object38)
	(predicate0 object18 object43)
	(predicate0 object18 object48)
	(predicate0 object23 object28)
	(predicate0 object23 object33)
	(predicate0 object23 object38)
	(predicate0 object23 object43)
	(predicate0 object23 object48)
	(predicate0 object28 object33)
	(predicate0 object28 object38)
	(predicate0 object28 object43)
	(predicate0 object28 object48)
	(predicate0 object33 object38)
	(predicate0 object33 object43)
	(predicate0 object33 object48)
	(predicate0 object38 object43)
	(predicate0 object38 object48)
	(predicate0 object43 object48)
	(predicate0 object4 object9)
	(predicate0 object4 object14)
	(predicate0 object4 object19)
	(predicate0 object4 object24)
	(predicate0 object4 object29)
	(predicate0 object4 object34)
	(predicate0 object4 object39)
	(predicate0 object4 object44)
	(predicate0 object4 object49)
	(predicate0 object9 object14)
	(predicate0 object9 object19)
	(predicate0 object9 object24)
	(predicate0 object9 object29)
	(predicate0 object9 object34)
	(predicate0 object9 object39)
	(predicate0 object9 object44)
	(predicate0 object9 object49)
	(predicate0 object14 object19)
	(predicate0 object14 object24)
	(predicate0 object14 object29)
	(predicate0 object14 object34)
	(predicate0 object14 object39)
	(predicate0 object14 object44)
	(predicate0 object14 object49)
	(predicate0 object19 object24)
	(predicate0 object19 object29)
	(predicate0 object19 object34)
	(predicate0 object19 object39)
	(predicate0 object19 object44)
	(predicate0 object19 object49)
	(predicate0 object24 object29)
	(predicate0 object24 object34)
	(predicate0 object24 object39)
	(predicate0 object24 object44)
	(predicate0 object24 object49)
	(predicate0 object29 object34)
	(predicate0 object29 object39)
	(predicate0 object29 object44)
	(predicate0 object29 object49)
	(predicate0 object34 object39)
	(predicate0 object34 object44)
	(predicate0 object34 object49)
	(predicate0 object39 object44)
	(predicate0 object39 object49)
	(predicate0 object44 object49)

	(predicate7 object50 object40)
	(predicate4 object50 object15)
	(predicate7 object55 object5)
	(predicate4 object55 object0)
	(predicate7 object60 object35)
	(predicate4 object60 object40)
	(predicate7 object65 object25)
	(predicate4 object65 object10)
	(predicate7 object70 object45)
	(predicate4 object70 object20)
	(predicate7 object75 object20)
	(predicate4 object75 object0)
	(predicate7 object80 object10)
	(predicate4 object80 object15)
	(predicate7 object51 object36)
	(predicate4 object51 object31)
	(predicate7 object56 object26)
	(predicate4 object56 object21)
	(predicate7 object61 object21)
	(predicate4 object61 object26)
	(predicate7 object66 object41)
	(predicate4 object66 object21)
	(predicate7 object71 object16)
	(predicate4 object71 object21)
	(predicate7 object76 object11)
	(predicate4 object76 object41)
	(predicate7 object81 object46)
	(predicate4 object81 object6)
	(predicate7 object52 object12)
	(predicate4 object52 object17)
	(predicate7 object57 object7)
	(predicate4 object57 object22)
	(predicate7 object62 object47)
	(predicate4 object62 object42)
	(predicate7 object67 object17)
	(predicate4 object67 object42)
	(predicate7 object72 object27)
	(predicate4 object72 object42)
	(predicate7 object77 object37)
	(predicate4 object77 object12)
	(predicate7 object82 object22)
	(predicate4 object82 object17)
	(predicate7 object53 object8)
	(predicate4 object53 object18)
	(predicate7 object58 object33)
	(predicate4 object58 object48)
	(predicate7 object63 object13)
	(predicate4 object63 object33)
	(predicate7 object68 object18)
	(predicate4 object68 object33)
	(predicate7 object73 object28)
	(predicate4 object73 object18)
	(predicate7 object78 object3)
	(predicate4 object78 object38)
	(predicate7 object83 object48)
	(predicate4 object83 object33)
	(predicate7 object54 object44)
	(predicate4 object54 object19)
	(predicate7 object59 object34)
	(predicate4 object59 object24)
	(predicate7 object64 object29)
	(predicate4 object64 object4)
	(predicate7 object69 object19)
	(predicate4 object69 object29)
	(predicate7 object74 object39)
	(predicate4 object74 object29)
	(predicate7 object79 object9)
	(predicate4 object79 object49)
	(predicate7 object84 object14)
	(predicate4 object84 object9)

	(predicate6 object20)
	(predicate6 object16)
	(predicate6 object32)
	(predicate6 object33)
	(predicate6 object39)
)

(:goal (and
	(predicate8 object50)
	(predicate8 object55)
	(predicate8 object60)
	(predicate8 object65)
	(predicate8 object70)
	(predicate8 object75)
	(predicate8 object80)
	(predicate8 object51)
	(predicate8 object56)
	(predicate8 object61)
	(predicate8 object66)
	(predicate8 object71)
	(predicate8 object76)
	(predicate8 object81)
	(predicate8 object52)
	(predicate8 object57)
	(predicate8 object62)
	(predicate8 object67)
	(predicate8 object72)
	(predicate8 object77)
	(predicate8 object82)
	(predicate8 object53)
	(predicate8 object58)
	(predicate8 object63)
	(predicate8 object68)
	(predicate8 object73)
	(predicate8 object78)
	(predicate8 object83)
	(predicate8 object54)
	(predicate8 object59)
	(predicate8 object64)
	(predicate8 object69)
	(predicate8 object74)
	(predicate8 object79)
	(predicate8 object84)
))
)

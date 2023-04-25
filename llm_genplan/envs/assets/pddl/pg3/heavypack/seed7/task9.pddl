(define (problem heavy-pack-prob)
	(:domain heavy-pack)
	(:objects o14 o300 o672)

(:init
    (box-empty)
    (unpacked o14)
    (unpacked o300)
    (unpacked o672)
    (heavier o14 o300)
    (heavier o14 o672)
    (heavier o300 o672)
)

(:goal (and (packed o14) (packed o300) (packed o672)))
)

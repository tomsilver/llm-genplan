(define (problem heavy-pack-prob)
	(:domain heavy-pack)
	(:objects o124 o28 o5 o526 o671 o8)

(:init
    (box-empty)
    (unpacked o124)
    (unpacked o28)
    (unpacked o5)
    (unpacked o526)
    (unpacked o671)
    (unpacked o8)
    (heavier o526 o8)
    (heavier o526 o671)
    (heavier o526 o124)
    (heavier o526 o28)
    (heavier o526 o5)
    (heavier o8 o671)
    (heavier o8 o124)
    (heavier o8 o28)
    (heavier o8 o5)
    (heavier o671 o124)
    (heavier o671 o28)
    (heavier o671 o5)
    (heavier o124 o28)
    (heavier o124 o5)
    (heavier o28 o5)
)

(:goal (and (packed o124) (packed o28) (packed o5) (packed o526) (packed o671) (packed o8)))
)
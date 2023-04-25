(define (problem heavy-pack-prob)
	(:domain heavy-pack)
	(:objects o1000 o148 o191)

(:init
    (box-empty)
    (unpacked o1000)
    (unpacked o148)
    (unpacked o191)
    (heavier o191 o1000)
    (heavier o191 o148)
    (heavier o1000 o148)
)

(:goal (and (packed o1000) (packed o148) (packed o191)))
)

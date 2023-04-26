(define (problem heavy-pack-prob)
	(:domain heavy-pack)
	(:objects o221 o612 o7)

(:init
    (box-empty)
    (unpacked o221)
    (unpacked o612)
    (unpacked o7)
    (heavier o612 o7)
    (heavier o612 o221)
    (heavier o7 o221)
)

(:goal (and (packed o221) (packed o612) (packed o7)))
)

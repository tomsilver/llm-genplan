(define (problem heavy-pack-prob)
	(:domain heavy-pack)
	(:objects o370 o594 o745)

(:init
    (box-empty)
    (unpacked o370)
    (unpacked o594)
    (unpacked o745)
    (heavier o745 o370)
    (heavier o745 o594)
    (heavier o370 o594)
)

(:goal (and (packed o370) (packed o594) (packed o745)))
)

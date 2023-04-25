(define (problem heavy-pack-prob)
	(:domain heavy-pack)
	(:objects o404 o570 o997)

(:init
    (box-empty)
    (unpacked o404)
    (unpacked o570)
    (unpacked o997)
    (heavier o997 o404)
    (heavier o997 o570)
    (heavier o404 o570)
)

(:goal (and (packed o404) (packed o570) (packed o997)))
)

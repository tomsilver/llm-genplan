(define (problem heavy-pack-prob)
	(:domain heavy-pack)
	(:objects o153 o304 o348 o376 o851)

(:init
    (box-empty)
    (unpacked o153)
    (unpacked o304)
    (unpacked o348)
    (unpacked o376)
    (unpacked o851)
    (heavier o304 o851)
    (heavier o304 o153)
    (heavier o304 o376)
    (heavier o304 o348)
    (heavier o851 o153)
    (heavier o851 o376)
    (heavier o851 o348)
    (heavier o153 o376)
    (heavier o153 o348)
    (heavier o376 o348)
)

(:goal (and (packed o153) (packed o304) (packed o348) (packed o376) (packed o851)))
)

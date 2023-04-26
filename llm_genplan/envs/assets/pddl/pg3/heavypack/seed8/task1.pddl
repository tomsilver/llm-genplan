(define (problem heavy-pack-prob)
	(:domain heavy-pack)
	(:objects o479 o543 o959)

(:init
    (box-empty)
    (unpacked o479)
    (unpacked o543)
    (unpacked o959)
    (heavier o479 o959)
    (heavier o479 o543)
    (heavier o959 o543)
)

(:goal (and (packed o479) (packed o543) (packed o959)))
)

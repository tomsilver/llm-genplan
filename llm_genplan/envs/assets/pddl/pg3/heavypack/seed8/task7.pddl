(define (problem heavy-pack-prob)
	(:domain heavy-pack)
	(:objects o375 o417 o502)

(:init
    (box-empty)
    (unpacked o375)
    (unpacked o417)
    (unpacked o502)
    (heavier o417 o502)
    (heavier o417 o375)
    (heavier o502 o375)
)

(:goal (and (packed o375) (packed o417) (packed o502)))
)

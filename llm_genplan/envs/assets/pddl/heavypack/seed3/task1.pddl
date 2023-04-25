(define (problem heavy-pack-prob)
	(:domain heavy-pack)
	(:objects o113 o391 o452)

(:init
    (box-empty)
    (unpacked o113)
    (unpacked o391)
    (unpacked o452)
    (heavier o452 o113)
    (heavier o452 o391)
    (heavier o113 o391)
)

(:goal (and (packed o113) (packed o391) (packed o452)))
)

(define (problem heavy-pack-prob)
	(:domain heavy-pack)
	(:objects o177 o377 o624)

(:init
    (box-empty)
    (unpacked o177)
    (unpacked o377)
    (unpacked o624)
    (heavier o177 o377)
    (heavier o177 o624)
    (heavier o377 o624)
)

(:goal (and (packed o177) (packed o377) (packed o624)))
)

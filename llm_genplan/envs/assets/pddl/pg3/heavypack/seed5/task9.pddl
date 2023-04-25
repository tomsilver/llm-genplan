(define (problem heavy-pack-prob)
	(:domain heavy-pack)
	(:objects o162 o692 o841)

(:init
    (box-empty)
    (unpacked o162)
    (unpacked o692)
    (unpacked o841)
    (heavier o162 o841)
    (heavier o162 o692)
    (heavier o841 o692)
)

(:goal (and (packed o162) (packed o692) (packed o841)))
)

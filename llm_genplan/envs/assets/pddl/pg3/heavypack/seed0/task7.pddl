(define (problem heavy-pack-prob)
	(:domain heavy-pack)
	(:objects o58 o79 o792 o877)

(:init
    (box-empty)
    (unpacked o58)
    (unpacked o79)
    (unpacked o792)
    (unpacked o877)
    (heavier o79 o58)
    (heavier o79 o877)
    (heavier o79 o792)
    (heavier o58 o877)
    (heavier o58 o792)
    (heavier o877 o792)
)

(:goal (and (packed o58) (packed o79) (packed o792) (packed o877)))
)
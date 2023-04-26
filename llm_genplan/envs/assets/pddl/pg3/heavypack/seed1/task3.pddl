(define (problem heavy-pack-prob)
	(:domain heavy-pack)
	(:objects o117 o280 o485 o498 o62 o749 o92 o962 o981)

(:init
    (box-empty)
    (unpacked o117)
    (unpacked o280)
    (unpacked o485)
    (unpacked o498)
    (unpacked o62)
    (unpacked o749)
    (unpacked o92)
    (unpacked o962)
    (unpacked o981)
    (heavier o117 o498)
    (heavier o117 o962)
    (heavier o117 o92)
    (heavier o117 o749)
    (heavier o117 o280)
    (heavier o117 o981)
    (heavier o117 o485)
    (heavier o117 o62)
    (heavier o498 o962)
    (heavier o498 o92)
    (heavier o498 o749)
    (heavier o498 o280)
    (heavier o498 o981)
    (heavier o498 o485)
    (heavier o498 o62)
    (heavier o962 o92)
    (heavier o962 o749)
    (heavier o962 o280)
    (heavier o962 o981)
    (heavier o962 o485)
    (heavier o962 o62)
    (heavier o92 o749)
    (heavier o92 o280)
    (heavier o92 o981)
    (heavier o92 o485)
    (heavier o92 o62)
    (heavier o749 o280)
    (heavier o749 o981)
    (heavier o749 o485)
    (heavier o749 o62)
    (heavier o280 o981)
    (heavier o280 o485)
    (heavier o280 o62)
    (heavier o981 o485)
    (heavier o981 o62)
    (heavier o485 o62)
)

(:goal (and (packed o117) (packed o280) (packed o485) (packed o498) (packed o62) (packed o749) (packed o92) (packed o962) (packed o981)))
)
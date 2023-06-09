(define (problem heavy-pack-prob)
	(:domain heavy-pack)
	(:objects o253 o254 o30 o374 o474 o520 o609 o707 o90)

(:init
    (box-empty)
    (unpacked o253)
    (unpacked o254)
    (unpacked o30)
    (unpacked o374)
    (unpacked o474)
    (unpacked o520)
    (unpacked o609)
    (unpacked o707)
    (unpacked o90)
    (heavier o520 o253)
    (heavier o520 o374)
    (heavier o520 o474)
    (heavier o520 o707)
    (heavier o520 o30)
    (heavier o520 o609)
    (heavier o520 o254)
    (heavier o520 o90)
    (heavier o253 o374)
    (heavier o253 o474)
    (heavier o253 o707)
    (heavier o253 o30)
    (heavier o253 o609)
    (heavier o253 o254)
    (heavier o253 o90)
    (heavier o374 o474)
    (heavier o374 o707)
    (heavier o374 o30)
    (heavier o374 o609)
    (heavier o374 o254)
    (heavier o374 o90)
    (heavier o474 o707)
    (heavier o474 o30)
    (heavier o474 o609)
    (heavier o474 o254)
    (heavier o474 o90)
    (heavier o707 o30)
    (heavier o707 o609)
    (heavier o707 o254)
    (heavier o707 o90)
    (heavier o30 o609)
    (heavier o30 o254)
    (heavier o30 o90)
    (heavier o609 o254)
    (heavier o609 o90)
    (heavier o254 o90)
)

(:goal (and (packed o253) (packed o254) (packed o30) (packed o374) (packed o474) (packed o520) (packed o609) (packed o707) (packed o90)))
)

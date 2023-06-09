(define (problem heavy-pack-prob)
	(:domain heavy-pack)
	(:objects o225 o285 o300 o55 o578 o625 o684 o776 o834 o898)

(:init
    (box-empty)
    (unpacked o225)
    (unpacked o285)
    (unpacked o300)
    (unpacked o55)
    (unpacked o578)
    (unpacked o625)
    (unpacked o684)
    (unpacked o776)
    (unpacked o834)
    (unpacked o898)
    (heavier o578 o300)
    (heavier o578 o834)
    (heavier o578 o55)
    (heavier o578 o898)
    (heavier o578 o285)
    (heavier o578 o625)
    (heavier o578 o684)
    (heavier o578 o225)
    (heavier o578 o776)
    (heavier o300 o834)
    (heavier o300 o55)
    (heavier o300 o898)
    (heavier o300 o285)
    (heavier o300 o625)
    (heavier o300 o684)
    (heavier o300 o225)
    (heavier o300 o776)
    (heavier o834 o55)
    (heavier o834 o898)
    (heavier o834 o285)
    (heavier o834 o625)
    (heavier o834 o684)
    (heavier o834 o225)
    (heavier o834 o776)
    (heavier o55 o898)
    (heavier o55 o285)
    (heavier o55 o625)
    (heavier o55 o684)
    (heavier o55 o225)
    (heavier o55 o776)
    (heavier o898 o285)
    (heavier o898 o625)
    (heavier o898 o684)
    (heavier o898 o225)
    (heavier o898 o776)
    (heavier o285 o625)
    (heavier o285 o684)
    (heavier o285 o225)
    (heavier o285 o776)
    (heavier o625 o684)
    (heavier o625 o225)
    (heavier o625 o776)
    (heavier o684 o225)
    (heavier o684 o776)
    (heavier o225 o776)
)

(:goal (and (packed o225) (packed o285) (packed o300) (packed o55) (packed o578) (packed o625) (packed o684) (packed o776) (packed o834) (packed o898)))
)

(define (problem heavy-pack-prob)
	(:domain heavy-pack)
	(:objects o175 o33 o730 o765 o847 o864 o89)

(:init
    (box-empty)
    (unpacked o175)
    (unpacked o33)
    (unpacked o730)
    (unpacked o765)
    (unpacked o847)
    (unpacked o864)
    (unpacked o89)
    (heavier o765 o730)
    (heavier o765 o864)
    (heavier o765 o847)
    (heavier o765 o175)
    (heavier o765 o33)
    (heavier o765 o89)
    (heavier o730 o864)
    (heavier o730 o847)
    (heavier o730 o175)
    (heavier o730 o33)
    (heavier o730 o89)
    (heavier o864 o847)
    (heavier o864 o175)
    (heavier o864 o33)
    (heavier o864 o89)
    (heavier o847 o175)
    (heavier o847 o33)
    (heavier o847 o89)
    (heavier o175 o33)
    (heavier o175 o89)
    (heavier o33 o89)
)

(:goal (and (packed o175) (packed o33) (packed o730) (packed o765) (packed o847) (packed o864) (packed o89)))
)

(define (problem heavy-pack-prob)
	(:domain heavy-pack)
	(:objects o450 o797 o860 o895)

(:init
    (box-empty)
    (unpacked o450)
    (unpacked o797)
    (unpacked o860)
    (unpacked o895)
    (heavier o797 o860)
    (heavier o797 o895)
    (heavier o797 o450)
    (heavier o860 o895)
    (heavier o860 o450)
    (heavier o895 o450)
)

(:goal (and (packed o450) (packed o797) (packed o860) (packed o895)))
)

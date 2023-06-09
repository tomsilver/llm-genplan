(define (problem heavy-pack-prob)
	(:domain heavy-pack)
	(:objects o160 o215 o341 o466 o622 o700 o845 o858 o989)

(:init
    (box-empty)
    (unpacked o160)
    (unpacked o215)
    (unpacked o341)
    (unpacked o466)
    (unpacked o622)
    (unpacked o700)
    (unpacked o845)
    (unpacked o858)
    (unpacked o989)
    (heavier o858 o341)
    (heavier o858 o466)
    (heavier o858 o160)
    (heavier o858 o989)
    (heavier o858 o215)
    (heavier o858 o845)
    (heavier o858 o622)
    (heavier o858 o700)
    (heavier o341 o466)
    (heavier o341 o160)
    (heavier o341 o989)
    (heavier o341 o215)
    (heavier o341 o845)
    (heavier o341 o622)
    (heavier o341 o700)
    (heavier o466 o160)
    (heavier o466 o989)
    (heavier o466 o215)
    (heavier o466 o845)
    (heavier o466 o622)
    (heavier o466 o700)
    (heavier o160 o989)
    (heavier o160 o215)
    (heavier o160 o845)
    (heavier o160 o622)
    (heavier o160 o700)
    (heavier o989 o215)
    (heavier o989 o845)
    (heavier o989 o622)
    (heavier o989 o700)
    (heavier o215 o845)
    (heavier o215 o622)
    (heavier o215 o700)
    (heavier o845 o622)
    (heavier o845 o700)
    (heavier o622 o700)
)

(:goal (and (packed o160) (packed o215) (packed o341) (packed o466) (packed o622) (packed o700) (packed o845) (packed o858) (packed o989)))
)

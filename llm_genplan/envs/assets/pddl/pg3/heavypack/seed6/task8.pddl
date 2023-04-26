(define (problem heavy-pack-prob)
	(:domain heavy-pack)
	(:objects o198 o281 o397 o434 o526 o573 o59 o892)

(:init
    (box-empty)
    (unpacked o198)
    (unpacked o281)
    (unpacked o397)
    (unpacked o434)
    (unpacked o526)
    (unpacked o573)
    (unpacked o59)
    (unpacked o892)
    (heavier o526 o397)
    (heavier o526 o434)
    (heavier o526 o573)
    (heavier o526 o59)
    (heavier o526 o198)
    (heavier o526 o892)
    (heavier o526 o281)
    (heavier o397 o434)
    (heavier o397 o573)
    (heavier o397 o59)
    (heavier o397 o198)
    (heavier o397 o892)
    (heavier o397 o281)
    (heavier o434 o573)
    (heavier o434 o59)
    (heavier o434 o198)
    (heavier o434 o892)
    (heavier o434 o281)
    (heavier o573 o59)
    (heavier o573 o198)
    (heavier o573 o892)
    (heavier o573 o281)
    (heavier o59 o198)
    (heavier o59 o892)
    (heavier o59 o281)
    (heavier o198 o892)
    (heavier o198 o281)
    (heavier o892 o281)
)

(:goal (and (packed o198) (packed o281) (packed o397) (packed o434) (packed o526) (packed o573) (packed o59) (packed o892)))
)
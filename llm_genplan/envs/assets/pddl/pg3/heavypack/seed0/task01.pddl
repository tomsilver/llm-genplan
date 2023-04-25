(define (problem heavy-pack-prob1)
	(:domain heavy-pack)
	(:objects o1 o2 o3 o4
	)

(:init
	(box-empty)

	(unpacked o1)
	(unpacked o2)
	(unpacked o3)
	(unpacked o4)

	(heavier o2 o4)
	(heavier o2 o3)
	(heavier o2 o1)
	(heavier o3 o4)
	(heavier o3 o1)
	(heavier o4 o1)

)

(:goal (and (packed o1) (packed o2) (packed o3) (packed o4)))
)

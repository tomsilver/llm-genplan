(define (problem heavy-pack-prob)
	(:domain heavy-pack)
	(:objects o1 o293 o696 o76 o870 o939 o944 o974)

(:init
    (box-empty)
    (unpacked o1)
    (unpacked o293)
    (unpacked o696)
    (unpacked o76)
    (unpacked o870)
    (unpacked o939)
    (unpacked o944)
    (unpacked o974)
    (heavier o1 o870)
    (heavier o1 o974)
    (heavier o1 o76)
    (heavier o1 o293)
    (heavier o1 o944)
    (heavier o1 o696)
    (heavier o1 o939)
    (heavier o870 o974)
    (heavier o870 o76)
    (heavier o870 o293)
    (heavier o870 o944)
    (heavier o870 o696)
    (heavier o870 o939)
    (heavier o974 o76)
    (heavier o974 o293)
    (heavier o974 o944)
    (heavier o974 o696)
    (heavier o974 o939)
    (heavier o76 o293)
    (heavier o76 o944)
    (heavier o76 o696)
    (heavier o76 o939)
    (heavier o293 o944)
    (heavier o293 o696)
    (heavier o293 o939)
    (heavier o944 o696)
    (heavier o944 o939)
    (heavier o696 o939)
)

(:goal (and (packed o1) (packed o293) (packed o696) (packed o76) (packed o870) (packed o939) (packed o944) (packed o974)))
)

(define (problem heavy-pack-prob)
	(:domain heavy-pack)
	(:objects o14 o236 o290 o314 o506 o507 o520 o768 o968)

(:init
    (box-empty)
    (unpacked o14)
    (unpacked o236)
    (unpacked o290)
    (unpacked o314)
    (unpacked o506)
    (unpacked o507)
    (unpacked o520)
    (unpacked o768)
    (unpacked o968)
    (heavier o236 o768)
    (heavier o236 o290)
    (heavier o236 o14)
    (heavier o236 o520)
    (heavier o236 o968)
    (heavier o236 o507)
    (heavier o236 o506)
    (heavier o236 o314)
    (heavier o768 o290)
    (heavier o768 o14)
    (heavier o768 o520)
    (heavier o768 o968)
    (heavier o768 o507)
    (heavier o768 o506)
    (heavier o768 o314)
    (heavier o290 o14)
    (heavier o290 o520)
    (heavier o290 o968)
    (heavier o290 o507)
    (heavier o290 o506)
    (heavier o290 o314)
    (heavier o14 o520)
    (heavier o14 o968)
    (heavier o14 o507)
    (heavier o14 o506)
    (heavier o14 o314)
    (heavier o520 o968)
    (heavier o520 o507)
    (heavier o520 o506)
    (heavier o520 o314)
    (heavier o968 o507)
    (heavier o968 o506)
    (heavier o968 o314)
    (heavier o507 o506)
    (heavier o507 o314)
    (heavier o506 o314)
)

(:goal (and (packed o14) (packed o236) (packed o290) (packed o314) (packed o506) (packed o507) (packed o520) (packed o768) (packed o968)))
)

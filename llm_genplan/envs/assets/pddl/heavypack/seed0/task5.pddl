(define (problem heavy-pack-prob)
	(:domain heavy-pack)
	(:objects o358 o531 o719 o73 o890 o934)

(:init
    (box-empty)
    (unpacked o358)
    (unpacked o531)
    (unpacked o719)
    (unpacked o73)
    (unpacked o890)
    (unpacked o934)
    (heavier o719 o890)
    (heavier o719 o358)
    (heavier o719 o934)
    (heavier o719 o73)
    (heavier o719 o531)
    (heavier o890 o358)
    (heavier o890 o934)
    (heavier o890 o73)
    (heavier o890 o531)
    (heavier o358 o934)
    (heavier o358 o73)
    (heavier o358 o531)
    (heavier o934 o73)
    (heavier o934 o531)
    (heavier o73 o531)
)

(:goal (and (packed o358) (packed o531) (packed o719) (packed o73) (packed o890) (packed o934)))
)

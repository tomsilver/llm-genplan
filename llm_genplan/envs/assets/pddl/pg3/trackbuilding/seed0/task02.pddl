(define (problem track-building-prob2)
	(:domain track-building)
	(:objects
		x0-y0
		x1-y0
		x2-y0
		x3-y0
		x0-y1
		x1-y1
		x2-y1
		x3-y1
		x0-y2
		x1-y2
		x2-y2
		x3-y2
		x0-y3
		x1-y3
		x2-y3
		x3-y3
	)

(:init
	(agent-at x0-y0)
	(train-at x2-y0)
	(forward x0-y0 x0-y1)
	(forward x0-y1 x0-y2)
	(forward x0-y2 x0-y3)
	(forward x1-y0 x1-y1)
	(forward x1-y1 x1-y2)
	(forward x1-y2 x1-y3)
	(forward x2-y0 x2-y1)
	(forward x2-y1 x2-y2)
	(forward x2-y2 x2-y3)
	(forward x3-y0 x3-y1)
	(forward x3-y1 x3-y2)
	(forward x3-y2 x3-y3)

)

(:goal (and (train-at x2-y3)))
)

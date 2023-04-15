(define (problem miconicprob)
	(:domain miconic)
	(:objects
		f0_b0 - floor
		f1_b0 - floor
		f2_b0 - floor
		f3_b0 - floor
		f4_b0 - floor
		f5_b0 - floor
		f6_b0 - floor
		f7_b0 - floor
		f8_b0 - floor
		f9_b0 - floor
		p0_b0 - passenger
		p1_b0 - passenger
		p2_b0 - passenger
		p3_b0 - passenger
		p4_b0 - passenger
	)

(:init
	(above f0_b0 f1_b0)
	(above f0_b0 f2_b0)
	(above f0_b0 f3_b0)
	(above f0_b0 f4_b0)
	(above f0_b0 f5_b0)
	(above f0_b0 f6_b0)
	(above f0_b0 f7_b0)
	(above f0_b0 f8_b0)
	(above f0_b0 f9_b0)
	(above f1_b0 f2_b0)
	(above f1_b0 f3_b0)
	(above f1_b0 f4_b0)
	(above f1_b0 f5_b0)
	(above f1_b0 f6_b0)
	(above f1_b0 f7_b0)
	(above f1_b0 f8_b0)
	(above f1_b0 f9_b0)
	(above f2_b0 f3_b0)
	(above f2_b0 f4_b0)
	(above f2_b0 f5_b0)
	(above f2_b0 f6_b0)
	(above f2_b0 f7_b0)
	(above f2_b0 f8_b0)
	(above f2_b0 f9_b0)
	(above f3_b0 f4_b0)
	(above f3_b0 f5_b0)
	(above f3_b0 f6_b0)
	(above f3_b0 f7_b0)
	(above f3_b0 f8_b0)
	(above f3_b0 f9_b0)
	(above f4_b0 f5_b0)
	(above f4_b0 f6_b0)
	(above f4_b0 f7_b0)
	(above f4_b0 f8_b0)
	(above f4_b0 f9_b0)
	(above f5_b0 f6_b0)
	(above f5_b0 f7_b0)
	(above f5_b0 f8_b0)
	(above f5_b0 f9_b0)
	(above f6_b0 f7_b0)
	(above f6_b0 f8_b0)
	(above f6_b0 f9_b0)
	(above f7_b0 f8_b0)
	(above f7_b0 f9_b0)
	(above f8_b0 f9_b0)

	(origin p0_b0 f6_b0)
	(destin p0_b0 f5_b0)
	(origin p1_b0 f1_b0)
	(destin p1_b0 f6_b0)
	(origin p2_b0 f8_b0)
	(destin p2_b0 f4_b0)
	(origin p3_b0 f4_b0)
	(destin p3_b0 f1_b0)
	(origin p4_b0 f2_b0)
	(destin p4_b0 f5_b0)

	(lift-at f1_b0)
)

(:goal (and
	(served p0_b0)
	(served p1_b0)
	(served p2_b0)
	(served p3_b0)
	(served p4_b0)
))
)

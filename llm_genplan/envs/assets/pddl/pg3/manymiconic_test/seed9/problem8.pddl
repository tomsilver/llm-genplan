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
		f10_b0 - floor
		f11_b0 - floor
		f12_b0 - floor
		p0_b0 - passenger
		f0_b1 - floor
		f1_b1 - floor
		f2_b1 - floor
		f3_b1 - floor
		f4_b1 - floor
		f5_b1 - floor
		f6_b1 - floor
		f7_b1 - floor
		f8_b1 - floor
		f9_b1 - floor
		f10_b1 - floor
		f11_b1 - floor
		f12_b1 - floor
		p0_b1 - passenger
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
	(above f0_b0 f10_b0)
	(above f0_b0 f11_b0)
	(above f0_b0 f12_b0)
	(above f1_b0 f2_b0)
	(above f1_b0 f3_b0)
	(above f1_b0 f4_b0)
	(above f1_b0 f5_b0)
	(above f1_b0 f6_b0)
	(above f1_b0 f7_b0)
	(above f1_b0 f8_b0)
	(above f1_b0 f9_b0)
	(above f1_b0 f10_b0)
	(above f1_b0 f11_b0)
	(above f1_b0 f12_b0)
	(above f2_b0 f3_b0)
	(above f2_b0 f4_b0)
	(above f2_b0 f5_b0)
	(above f2_b0 f6_b0)
	(above f2_b0 f7_b0)
	(above f2_b0 f8_b0)
	(above f2_b0 f9_b0)
	(above f2_b0 f10_b0)
	(above f2_b0 f11_b0)
	(above f2_b0 f12_b0)
	(above f3_b0 f4_b0)
	(above f3_b0 f5_b0)
	(above f3_b0 f6_b0)
	(above f3_b0 f7_b0)
	(above f3_b0 f8_b0)
	(above f3_b0 f9_b0)
	(above f3_b0 f10_b0)
	(above f3_b0 f11_b0)
	(above f3_b0 f12_b0)
	(above f4_b0 f5_b0)
	(above f4_b0 f6_b0)
	(above f4_b0 f7_b0)
	(above f4_b0 f8_b0)
	(above f4_b0 f9_b0)
	(above f4_b0 f10_b0)
	(above f4_b0 f11_b0)
	(above f4_b0 f12_b0)
	(above f5_b0 f6_b0)
	(above f5_b0 f7_b0)
	(above f5_b0 f8_b0)
	(above f5_b0 f9_b0)
	(above f5_b0 f10_b0)
	(above f5_b0 f11_b0)
	(above f5_b0 f12_b0)
	(above f6_b0 f7_b0)
	(above f6_b0 f8_b0)
	(above f6_b0 f9_b0)
	(above f6_b0 f10_b0)
	(above f6_b0 f11_b0)
	(above f6_b0 f12_b0)
	(above f7_b0 f8_b0)
	(above f7_b0 f9_b0)
	(above f7_b0 f10_b0)
	(above f7_b0 f11_b0)
	(above f7_b0 f12_b0)
	(above f8_b0 f9_b0)
	(above f8_b0 f10_b0)
	(above f8_b0 f11_b0)
	(above f8_b0 f12_b0)
	(above f9_b0 f10_b0)
	(above f9_b0 f11_b0)
	(above f9_b0 f12_b0)
	(above f10_b0 f11_b0)
	(above f10_b0 f12_b0)
	(above f11_b0 f12_b0)
	(above f0_b1 f1_b1)
	(above f0_b1 f2_b1)
	(above f0_b1 f3_b1)
	(above f0_b1 f4_b1)
	(above f0_b1 f5_b1)
	(above f0_b1 f6_b1)
	(above f0_b1 f7_b1)
	(above f0_b1 f8_b1)
	(above f0_b1 f9_b1)
	(above f0_b1 f10_b1)
	(above f0_b1 f11_b1)
	(above f0_b1 f12_b1)
	(above f1_b1 f2_b1)
	(above f1_b1 f3_b1)
	(above f1_b1 f4_b1)
	(above f1_b1 f5_b1)
	(above f1_b1 f6_b1)
	(above f1_b1 f7_b1)
	(above f1_b1 f8_b1)
	(above f1_b1 f9_b1)
	(above f1_b1 f10_b1)
	(above f1_b1 f11_b1)
	(above f1_b1 f12_b1)
	(above f2_b1 f3_b1)
	(above f2_b1 f4_b1)
	(above f2_b1 f5_b1)
	(above f2_b1 f6_b1)
	(above f2_b1 f7_b1)
	(above f2_b1 f8_b1)
	(above f2_b1 f9_b1)
	(above f2_b1 f10_b1)
	(above f2_b1 f11_b1)
	(above f2_b1 f12_b1)
	(above f3_b1 f4_b1)
	(above f3_b1 f5_b1)
	(above f3_b1 f6_b1)
	(above f3_b1 f7_b1)
	(above f3_b1 f8_b1)
	(above f3_b1 f9_b1)
	(above f3_b1 f10_b1)
	(above f3_b1 f11_b1)
	(above f3_b1 f12_b1)
	(above f4_b1 f5_b1)
	(above f4_b1 f6_b1)
	(above f4_b1 f7_b1)
	(above f4_b1 f8_b1)
	(above f4_b1 f9_b1)
	(above f4_b1 f10_b1)
	(above f4_b1 f11_b1)
	(above f4_b1 f12_b1)
	(above f5_b1 f6_b1)
	(above f5_b1 f7_b1)
	(above f5_b1 f8_b1)
	(above f5_b1 f9_b1)
	(above f5_b1 f10_b1)
	(above f5_b1 f11_b1)
	(above f5_b1 f12_b1)
	(above f6_b1 f7_b1)
	(above f6_b1 f8_b1)
	(above f6_b1 f9_b1)
	(above f6_b1 f10_b1)
	(above f6_b1 f11_b1)
	(above f6_b1 f12_b1)
	(above f7_b1 f8_b1)
	(above f7_b1 f9_b1)
	(above f7_b1 f10_b1)
	(above f7_b1 f11_b1)
	(above f7_b1 f12_b1)
	(above f8_b1 f9_b1)
	(above f8_b1 f10_b1)
	(above f8_b1 f11_b1)
	(above f8_b1 f12_b1)
	(above f9_b1 f10_b1)
	(above f9_b1 f11_b1)
	(above f9_b1 f12_b1)
	(above f10_b1 f11_b1)
	(above f10_b1 f12_b1)
	(above f11_b1 f12_b1)

	(origin p0_b0 f10_b0)
	(destin p0_b0 f11_b0)
	(origin p0_b1 f6_b1)
	(destin p0_b1 f4_b1)

	(lift-at f5_b0)
	(lift-at f10_b1)
)

(:goal (and
	(served p0_b0)
	(served p0_b1)
))
)

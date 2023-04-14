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
		f13_b0 - floor
		f14_b0 - floor
		f15_b0 - floor
		f16_b0 - floor
		f17_b0 - floor
		f18_b0 - floor
		p0_b0 - passenger
		p1_b0 - passenger
		p2_b0 - passenger
		p3_b0 - passenger
		p4_b0 - passenger
		p5_b0 - passenger
		p6_b0 - passenger
		p7_b0 - passenger
		p8_b0 - passenger
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
		f13_b1 - floor
		f14_b1 - floor
		f15_b1 - floor
		f16_b1 - floor
		f17_b1 - floor
		f18_b1 - floor
		p0_b1 - passenger
		p1_b1 - passenger
		p2_b1 - passenger
		p3_b1 - passenger
		p4_b1 - passenger
		p5_b1 - passenger
		p6_b1 - passenger
		p7_b1 - passenger
		p8_b1 - passenger
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
	(above f0_b0 f13_b0)
	(above f0_b0 f14_b0)
	(above f0_b0 f15_b0)
	(above f0_b0 f16_b0)
	(above f0_b0 f17_b0)
	(above f0_b0 f18_b0)
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
	(above f1_b0 f13_b0)
	(above f1_b0 f14_b0)
	(above f1_b0 f15_b0)
	(above f1_b0 f16_b0)
	(above f1_b0 f17_b0)
	(above f1_b0 f18_b0)
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
	(above f2_b0 f13_b0)
	(above f2_b0 f14_b0)
	(above f2_b0 f15_b0)
	(above f2_b0 f16_b0)
	(above f2_b0 f17_b0)
	(above f2_b0 f18_b0)
	(above f3_b0 f4_b0)
	(above f3_b0 f5_b0)
	(above f3_b0 f6_b0)
	(above f3_b0 f7_b0)
	(above f3_b0 f8_b0)
	(above f3_b0 f9_b0)
	(above f3_b0 f10_b0)
	(above f3_b0 f11_b0)
	(above f3_b0 f12_b0)
	(above f3_b0 f13_b0)
	(above f3_b0 f14_b0)
	(above f3_b0 f15_b0)
	(above f3_b0 f16_b0)
	(above f3_b0 f17_b0)
	(above f3_b0 f18_b0)
	(above f4_b0 f5_b0)
	(above f4_b0 f6_b0)
	(above f4_b0 f7_b0)
	(above f4_b0 f8_b0)
	(above f4_b0 f9_b0)
	(above f4_b0 f10_b0)
	(above f4_b0 f11_b0)
	(above f4_b0 f12_b0)
	(above f4_b0 f13_b0)
	(above f4_b0 f14_b0)
	(above f4_b0 f15_b0)
	(above f4_b0 f16_b0)
	(above f4_b0 f17_b0)
	(above f4_b0 f18_b0)
	(above f5_b0 f6_b0)
	(above f5_b0 f7_b0)
	(above f5_b0 f8_b0)
	(above f5_b0 f9_b0)
	(above f5_b0 f10_b0)
	(above f5_b0 f11_b0)
	(above f5_b0 f12_b0)
	(above f5_b0 f13_b0)
	(above f5_b0 f14_b0)
	(above f5_b0 f15_b0)
	(above f5_b0 f16_b0)
	(above f5_b0 f17_b0)
	(above f5_b0 f18_b0)
	(above f6_b0 f7_b0)
	(above f6_b0 f8_b0)
	(above f6_b0 f9_b0)
	(above f6_b0 f10_b0)
	(above f6_b0 f11_b0)
	(above f6_b0 f12_b0)
	(above f6_b0 f13_b0)
	(above f6_b0 f14_b0)
	(above f6_b0 f15_b0)
	(above f6_b0 f16_b0)
	(above f6_b0 f17_b0)
	(above f6_b0 f18_b0)
	(above f7_b0 f8_b0)
	(above f7_b0 f9_b0)
	(above f7_b0 f10_b0)
	(above f7_b0 f11_b0)
	(above f7_b0 f12_b0)
	(above f7_b0 f13_b0)
	(above f7_b0 f14_b0)
	(above f7_b0 f15_b0)
	(above f7_b0 f16_b0)
	(above f7_b0 f17_b0)
	(above f7_b0 f18_b0)
	(above f8_b0 f9_b0)
	(above f8_b0 f10_b0)
	(above f8_b0 f11_b0)
	(above f8_b0 f12_b0)
	(above f8_b0 f13_b0)
	(above f8_b0 f14_b0)
	(above f8_b0 f15_b0)
	(above f8_b0 f16_b0)
	(above f8_b0 f17_b0)
	(above f8_b0 f18_b0)
	(above f9_b0 f10_b0)
	(above f9_b0 f11_b0)
	(above f9_b0 f12_b0)
	(above f9_b0 f13_b0)
	(above f9_b0 f14_b0)
	(above f9_b0 f15_b0)
	(above f9_b0 f16_b0)
	(above f9_b0 f17_b0)
	(above f9_b0 f18_b0)
	(above f10_b0 f11_b0)
	(above f10_b0 f12_b0)
	(above f10_b0 f13_b0)
	(above f10_b0 f14_b0)
	(above f10_b0 f15_b0)
	(above f10_b0 f16_b0)
	(above f10_b0 f17_b0)
	(above f10_b0 f18_b0)
	(above f11_b0 f12_b0)
	(above f11_b0 f13_b0)
	(above f11_b0 f14_b0)
	(above f11_b0 f15_b0)
	(above f11_b0 f16_b0)
	(above f11_b0 f17_b0)
	(above f11_b0 f18_b0)
	(above f12_b0 f13_b0)
	(above f12_b0 f14_b0)
	(above f12_b0 f15_b0)
	(above f12_b0 f16_b0)
	(above f12_b0 f17_b0)
	(above f12_b0 f18_b0)
	(above f13_b0 f14_b0)
	(above f13_b0 f15_b0)
	(above f13_b0 f16_b0)
	(above f13_b0 f17_b0)
	(above f13_b0 f18_b0)
	(above f14_b0 f15_b0)
	(above f14_b0 f16_b0)
	(above f14_b0 f17_b0)
	(above f14_b0 f18_b0)
	(above f15_b0 f16_b0)
	(above f15_b0 f17_b0)
	(above f15_b0 f18_b0)
	(above f16_b0 f17_b0)
	(above f16_b0 f18_b0)
	(above f17_b0 f18_b0)
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
	(above f0_b1 f13_b1)
	(above f0_b1 f14_b1)
	(above f0_b1 f15_b1)
	(above f0_b1 f16_b1)
	(above f0_b1 f17_b1)
	(above f0_b1 f18_b1)
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
	(above f1_b1 f13_b1)
	(above f1_b1 f14_b1)
	(above f1_b1 f15_b1)
	(above f1_b1 f16_b1)
	(above f1_b1 f17_b1)
	(above f1_b1 f18_b1)
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
	(above f2_b1 f13_b1)
	(above f2_b1 f14_b1)
	(above f2_b1 f15_b1)
	(above f2_b1 f16_b1)
	(above f2_b1 f17_b1)
	(above f2_b1 f18_b1)
	(above f3_b1 f4_b1)
	(above f3_b1 f5_b1)
	(above f3_b1 f6_b1)
	(above f3_b1 f7_b1)
	(above f3_b1 f8_b1)
	(above f3_b1 f9_b1)
	(above f3_b1 f10_b1)
	(above f3_b1 f11_b1)
	(above f3_b1 f12_b1)
	(above f3_b1 f13_b1)
	(above f3_b1 f14_b1)
	(above f3_b1 f15_b1)
	(above f3_b1 f16_b1)
	(above f3_b1 f17_b1)
	(above f3_b1 f18_b1)
	(above f4_b1 f5_b1)
	(above f4_b1 f6_b1)
	(above f4_b1 f7_b1)
	(above f4_b1 f8_b1)
	(above f4_b1 f9_b1)
	(above f4_b1 f10_b1)
	(above f4_b1 f11_b1)
	(above f4_b1 f12_b1)
	(above f4_b1 f13_b1)
	(above f4_b1 f14_b1)
	(above f4_b1 f15_b1)
	(above f4_b1 f16_b1)
	(above f4_b1 f17_b1)
	(above f4_b1 f18_b1)
	(above f5_b1 f6_b1)
	(above f5_b1 f7_b1)
	(above f5_b1 f8_b1)
	(above f5_b1 f9_b1)
	(above f5_b1 f10_b1)
	(above f5_b1 f11_b1)
	(above f5_b1 f12_b1)
	(above f5_b1 f13_b1)
	(above f5_b1 f14_b1)
	(above f5_b1 f15_b1)
	(above f5_b1 f16_b1)
	(above f5_b1 f17_b1)
	(above f5_b1 f18_b1)
	(above f6_b1 f7_b1)
	(above f6_b1 f8_b1)
	(above f6_b1 f9_b1)
	(above f6_b1 f10_b1)
	(above f6_b1 f11_b1)
	(above f6_b1 f12_b1)
	(above f6_b1 f13_b1)
	(above f6_b1 f14_b1)
	(above f6_b1 f15_b1)
	(above f6_b1 f16_b1)
	(above f6_b1 f17_b1)
	(above f6_b1 f18_b1)
	(above f7_b1 f8_b1)
	(above f7_b1 f9_b1)
	(above f7_b1 f10_b1)
	(above f7_b1 f11_b1)
	(above f7_b1 f12_b1)
	(above f7_b1 f13_b1)
	(above f7_b1 f14_b1)
	(above f7_b1 f15_b1)
	(above f7_b1 f16_b1)
	(above f7_b1 f17_b1)
	(above f7_b1 f18_b1)
	(above f8_b1 f9_b1)
	(above f8_b1 f10_b1)
	(above f8_b1 f11_b1)
	(above f8_b1 f12_b1)
	(above f8_b1 f13_b1)
	(above f8_b1 f14_b1)
	(above f8_b1 f15_b1)
	(above f8_b1 f16_b1)
	(above f8_b1 f17_b1)
	(above f8_b1 f18_b1)
	(above f9_b1 f10_b1)
	(above f9_b1 f11_b1)
	(above f9_b1 f12_b1)
	(above f9_b1 f13_b1)
	(above f9_b1 f14_b1)
	(above f9_b1 f15_b1)
	(above f9_b1 f16_b1)
	(above f9_b1 f17_b1)
	(above f9_b1 f18_b1)
	(above f10_b1 f11_b1)
	(above f10_b1 f12_b1)
	(above f10_b1 f13_b1)
	(above f10_b1 f14_b1)
	(above f10_b1 f15_b1)
	(above f10_b1 f16_b1)
	(above f10_b1 f17_b1)
	(above f10_b1 f18_b1)
	(above f11_b1 f12_b1)
	(above f11_b1 f13_b1)
	(above f11_b1 f14_b1)
	(above f11_b1 f15_b1)
	(above f11_b1 f16_b1)
	(above f11_b1 f17_b1)
	(above f11_b1 f18_b1)
	(above f12_b1 f13_b1)
	(above f12_b1 f14_b1)
	(above f12_b1 f15_b1)
	(above f12_b1 f16_b1)
	(above f12_b1 f17_b1)
	(above f12_b1 f18_b1)
	(above f13_b1 f14_b1)
	(above f13_b1 f15_b1)
	(above f13_b1 f16_b1)
	(above f13_b1 f17_b1)
	(above f13_b1 f18_b1)
	(above f14_b1 f15_b1)
	(above f14_b1 f16_b1)
	(above f14_b1 f17_b1)
	(above f14_b1 f18_b1)
	(above f15_b1 f16_b1)
	(above f15_b1 f17_b1)
	(above f15_b1 f18_b1)
	(above f16_b1 f17_b1)
	(above f16_b1 f18_b1)
	(above f17_b1 f18_b1)

	(origin p0_b0 f4_b0)
	(destin p0_b0 f7_b0)
	(origin p1_b0 f10_b0)
	(destin p1_b0 f14_b0)
	(origin p2_b0 f11_b0)
	(destin p2_b0 f13_b0)
	(origin p3_b0 f1_b0)
	(destin p3_b0 f15_b0)
	(origin p4_b0 f5_b0)
	(destin p4_b0 f7_b0)
	(origin p5_b0 f7_b0)
	(destin p5_b0 f8_b0)
	(origin p6_b0 f17_b0)
	(destin p6_b0 f13_b0)
	(origin p7_b0 f9_b0)
	(destin p7_b0 f1_b0)
	(origin p8_b0 f18_b0)
	(destin p8_b0 f10_b0)
	(origin p0_b1 f11_b1)
	(destin p0_b1 f12_b1)
	(origin p1_b1 f13_b1)
	(destin p1_b1 f14_b1)
	(origin p2_b1 f12_b1)
	(destin p2_b1 f17_b1)
	(origin p3_b1 f16_b1)
	(destin p3_b1 f9_b1)
	(origin p4_b1 f15_b1)
	(destin p4_b1 f4_b1)
	(origin p5_b1 f9_b1)
	(destin p5_b1 f8_b1)
	(origin p6_b1 f14_b1)
	(destin p6_b1 f6_b1)
	(origin p7_b1 f10_b1)
	(destin p7_b1 f15_b1)
	(origin p8_b1 f8_b1)
	(destin p8_b1 f5_b1)

	(lift-at f17_b0)
	(lift-at f0_b1)
)

(:goal (and
	(served p0_b0)
	(served p1_b0)
	(served p2_b0)
	(served p3_b0)
	(served p4_b0)
	(served p5_b0)
	(served p6_b0)
	(served p7_b0)
	(served p8_b0)
	(served p0_b1)
	(served p1_b1)
	(served p2_b1)
	(served p3_b1)
	(served p4_b1)
	(served p5_b1)
	(served p6_b1)
	(served p7_b1)
	(served p8_b1)
))
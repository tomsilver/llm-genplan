
(define (problem hiking) (:domain hiking)
  (:objects
        r0_c0 - loc
	r0_c1 - loc
	r0_c10 - loc
	r0_c2 - loc
	r0_c3 - loc
	r0_c4 - loc
	r0_c5 - loc
	r0_c6 - loc
	r0_c7 - loc
	r0_c8 - loc
	r0_c9 - loc
	r10_c0 - loc
	r10_c1 - loc
	r10_c10 - loc
	r10_c2 - loc
	r10_c3 - loc
	r10_c4 - loc
	r10_c5 - loc
	r10_c6 - loc
	r10_c7 - loc
	r10_c8 - loc
	r10_c9 - loc
	r1_c0 - loc
	r1_c1 - loc
	r1_c10 - loc
	r1_c2 - loc
	r1_c3 - loc
	r1_c4 - loc
	r1_c5 - loc
	r1_c6 - loc
	r1_c7 - loc
	r1_c8 - loc
	r1_c9 - loc
	r2_c0 - loc
	r2_c1 - loc
	r2_c10 - loc
	r2_c2 - loc
	r2_c3 - loc
	r2_c4 - loc
	r2_c5 - loc
	r2_c6 - loc
	r2_c7 - loc
	r2_c8 - loc
	r2_c9 - loc
	r3_c0 - loc
	r3_c1 - loc
	r3_c10 - loc
	r3_c2 - loc
	r3_c3 - loc
	r3_c4 - loc
	r3_c5 - loc
	r3_c6 - loc
	r3_c7 - loc
	r3_c8 - loc
	r3_c9 - loc
	r4_c0 - loc
	r4_c1 - loc
	r4_c10 - loc
	r4_c2 - loc
	r4_c3 - loc
	r4_c4 - loc
	r4_c5 - loc
	r4_c6 - loc
	r4_c7 - loc
	r4_c8 - loc
	r4_c9 - loc
	r5_c0 - loc
	r5_c1 - loc
	r5_c10 - loc
	r5_c2 - loc
	r5_c3 - loc
	r5_c4 - loc
	r5_c5 - loc
	r5_c6 - loc
	r5_c7 - loc
	r5_c8 - loc
	r5_c9 - loc
	r6_c0 - loc
	r6_c1 - loc
	r6_c10 - loc
	r6_c2 - loc
	r6_c3 - loc
	r6_c4 - loc
	r6_c5 - loc
	r6_c6 - loc
	r6_c7 - loc
	r6_c8 - loc
	r6_c9 - loc
	r7_c0 - loc
	r7_c1 - loc
	r7_c10 - loc
	r7_c2 - loc
	r7_c3 - loc
	r7_c4 - loc
	r7_c5 - loc
	r7_c6 - loc
	r7_c7 - loc
	r7_c8 - loc
	r7_c9 - loc
	r8_c0 - loc
	r8_c1 - loc
	r8_c10 - loc
	r8_c2 - loc
	r8_c3 - loc
	r8_c4 - loc
	r8_c5 - loc
	r8_c6 - loc
	r8_c7 - loc
	r8_c8 - loc
	r8_c9 - loc
	r9_c0 - loc
	r9_c1 - loc
	r9_c10 - loc
	r9_c2 - loc
	r9_c3 - loc
	r9_c4 - loc
	r9_c5 - loc
	r9_c6 - loc
	r9_c7 - loc
	r9_c8 - loc
	r9_c9 - loc
  )
  (:init 
	(adjacent r0_c0 r0_c1)
	(adjacent r0_c0 r1_c0)
	(adjacent r0_c10 r0_c9)
	(adjacent r0_c10 r1_c10)
	(adjacent r0_c1 r0_c0)
	(adjacent r0_c1 r0_c2)
	(adjacent r0_c1 r1_c1)
	(adjacent r0_c2 r0_c1)
	(adjacent r0_c2 r0_c3)
	(adjacent r0_c2 r1_c2)
	(adjacent r0_c3 r0_c2)
	(adjacent r0_c3 r0_c4)
	(adjacent r0_c3 r1_c3)
	(adjacent r0_c4 r0_c3)
	(adjacent r0_c4 r0_c5)
	(adjacent r0_c4 r1_c4)
	(adjacent r0_c5 r0_c4)
	(adjacent r0_c5 r0_c6)
	(adjacent r0_c5 r1_c5)
	(adjacent r0_c6 r0_c5)
	(adjacent r0_c6 r0_c7)
	(adjacent r0_c6 r1_c6)
	(adjacent r0_c7 r0_c6)
	(adjacent r0_c7 r0_c8)
	(adjacent r0_c7 r1_c7)
	(adjacent r0_c8 r0_c7)
	(adjacent r0_c8 r0_c9)
	(adjacent r0_c8 r1_c8)
	(adjacent r0_c9 r0_c10)
	(adjacent r0_c9 r0_c8)
	(adjacent r0_c9 r1_c9)
	(adjacent r10_c0 r10_c1)
	(adjacent r10_c0 r9_c0)
	(adjacent r10_c10 r10_c9)
	(adjacent r10_c10 r9_c10)
	(adjacent r10_c1 r10_c0)
	(adjacent r10_c1 r10_c2)
	(adjacent r10_c1 r9_c1)
	(adjacent r10_c2 r10_c1)
	(adjacent r10_c2 r10_c3)
	(adjacent r10_c2 r9_c2)
	(adjacent r10_c3 r10_c2)
	(adjacent r10_c3 r10_c4)
	(adjacent r10_c3 r9_c3)
	(adjacent r10_c4 r10_c3)
	(adjacent r10_c4 r10_c5)
	(adjacent r10_c4 r9_c4)
	(adjacent r10_c5 r10_c4)
	(adjacent r10_c5 r10_c6)
	(adjacent r10_c5 r9_c5)
	(adjacent r10_c6 r10_c5)
	(adjacent r10_c6 r10_c7)
	(adjacent r10_c6 r9_c6)
	(adjacent r10_c7 r10_c6)
	(adjacent r10_c7 r10_c8)
	(adjacent r10_c7 r9_c7)
	(adjacent r10_c8 r10_c7)
	(adjacent r10_c8 r10_c9)
	(adjacent r10_c8 r9_c8)
	(adjacent r10_c9 r10_c10)
	(adjacent r10_c9 r10_c8)
	(adjacent r10_c9 r9_c9)
	(adjacent r1_c0 r0_c0)
	(adjacent r1_c0 r1_c1)
	(adjacent r1_c0 r2_c0)
	(adjacent r1_c10 r0_c10)
	(adjacent r1_c10 r1_c9)
	(adjacent r1_c10 r2_c10)
	(adjacent r1_c1 r0_c1)
	(adjacent r1_c1 r1_c0)
	(adjacent r1_c1 r1_c2)
	(adjacent r1_c1 r2_c1)
	(adjacent r1_c2 r0_c2)
	(adjacent r1_c2 r1_c1)
	(adjacent r1_c2 r1_c3)
	(adjacent r1_c2 r2_c2)
	(adjacent r1_c3 r0_c3)
	(adjacent r1_c3 r1_c2)
	(adjacent r1_c3 r1_c4)
	(adjacent r1_c3 r2_c3)
	(adjacent r1_c4 r0_c4)
	(adjacent r1_c4 r1_c3)
	(adjacent r1_c4 r1_c5)
	(adjacent r1_c4 r2_c4)
	(adjacent r1_c5 r0_c5)
	(adjacent r1_c5 r1_c4)
	(adjacent r1_c5 r1_c6)
	(adjacent r1_c5 r2_c5)
	(adjacent r1_c6 r0_c6)
	(adjacent r1_c6 r1_c5)
	(adjacent r1_c6 r1_c7)
	(adjacent r1_c6 r2_c6)
	(adjacent r1_c7 r0_c7)
	(adjacent r1_c7 r1_c6)
	(adjacent r1_c7 r1_c8)
	(adjacent r1_c7 r2_c7)
	(adjacent r1_c8 r0_c8)
	(adjacent r1_c8 r1_c7)
	(adjacent r1_c8 r1_c9)
	(adjacent r1_c8 r2_c8)
	(adjacent r1_c9 r0_c9)
	(adjacent r1_c9 r1_c10)
	(adjacent r1_c9 r1_c8)
	(adjacent r1_c9 r2_c9)
	(adjacent r2_c0 r1_c0)
	(adjacent r2_c0 r2_c1)
	(adjacent r2_c0 r3_c0)
	(adjacent r2_c10 r1_c10)
	(adjacent r2_c10 r2_c9)
	(adjacent r2_c10 r3_c10)
	(adjacent r2_c1 r1_c1)
	(adjacent r2_c1 r2_c0)
	(adjacent r2_c1 r2_c2)
	(adjacent r2_c1 r3_c1)
	(adjacent r2_c2 r1_c2)
	(adjacent r2_c2 r2_c1)
	(adjacent r2_c2 r2_c3)
	(adjacent r2_c2 r3_c2)
	(adjacent r2_c3 r1_c3)
	(adjacent r2_c3 r2_c2)
	(adjacent r2_c3 r2_c4)
	(adjacent r2_c3 r3_c3)
	(adjacent r2_c4 r1_c4)
	(adjacent r2_c4 r2_c3)
	(adjacent r2_c4 r2_c5)
	(adjacent r2_c4 r3_c4)
	(adjacent r2_c5 r1_c5)
	(adjacent r2_c5 r2_c4)
	(adjacent r2_c5 r2_c6)
	(adjacent r2_c5 r3_c5)
	(adjacent r2_c6 r1_c6)
	(adjacent r2_c6 r2_c5)
	(adjacent r2_c6 r2_c7)
	(adjacent r2_c6 r3_c6)
	(adjacent r2_c7 r1_c7)
	(adjacent r2_c7 r2_c6)
	(adjacent r2_c7 r2_c8)
	(adjacent r2_c7 r3_c7)
	(adjacent r2_c8 r1_c8)
	(adjacent r2_c8 r2_c7)
	(adjacent r2_c8 r2_c9)
	(adjacent r2_c8 r3_c8)
	(adjacent r2_c9 r1_c9)
	(adjacent r2_c9 r2_c10)
	(adjacent r2_c9 r2_c8)
	(adjacent r2_c9 r3_c9)
	(adjacent r3_c0 r2_c0)
	(adjacent r3_c0 r3_c1)
	(adjacent r3_c0 r4_c0)
	(adjacent r3_c10 r2_c10)
	(adjacent r3_c10 r3_c9)
	(adjacent r3_c10 r4_c10)
	(adjacent r3_c1 r2_c1)
	(adjacent r3_c1 r3_c0)
	(adjacent r3_c1 r3_c2)
	(adjacent r3_c1 r4_c1)
	(adjacent r3_c2 r2_c2)
	(adjacent r3_c2 r3_c1)
	(adjacent r3_c2 r3_c3)
	(adjacent r3_c2 r4_c2)
	(adjacent r3_c3 r2_c3)
	(adjacent r3_c3 r3_c2)
	(adjacent r3_c3 r3_c4)
	(adjacent r3_c3 r4_c3)
	(adjacent r3_c4 r2_c4)
	(adjacent r3_c4 r3_c3)
	(adjacent r3_c4 r3_c5)
	(adjacent r3_c4 r4_c4)
	(adjacent r3_c5 r2_c5)
	(adjacent r3_c5 r3_c4)
	(adjacent r3_c5 r3_c6)
	(adjacent r3_c5 r4_c5)
	(adjacent r3_c6 r2_c6)
	(adjacent r3_c6 r3_c5)
	(adjacent r3_c6 r3_c7)
	(adjacent r3_c6 r4_c6)
	(adjacent r3_c7 r2_c7)
	(adjacent r3_c7 r3_c6)
	(adjacent r3_c7 r3_c8)
	(adjacent r3_c7 r4_c7)
	(adjacent r3_c8 r2_c8)
	(adjacent r3_c8 r3_c7)
	(adjacent r3_c8 r3_c9)
	(adjacent r3_c8 r4_c8)
	(adjacent r3_c9 r2_c9)
	(adjacent r3_c9 r3_c10)
	(adjacent r3_c9 r3_c8)
	(adjacent r3_c9 r4_c9)
	(adjacent r4_c0 r3_c0)
	(adjacent r4_c0 r4_c1)
	(adjacent r4_c0 r5_c0)
	(adjacent r4_c10 r3_c10)
	(adjacent r4_c10 r4_c9)
	(adjacent r4_c10 r5_c10)
	(adjacent r4_c1 r3_c1)
	(adjacent r4_c1 r4_c0)
	(adjacent r4_c1 r4_c2)
	(adjacent r4_c1 r5_c1)
	(adjacent r4_c2 r3_c2)
	(adjacent r4_c2 r4_c1)
	(adjacent r4_c2 r4_c3)
	(adjacent r4_c2 r5_c2)
	(adjacent r4_c3 r3_c3)
	(adjacent r4_c3 r4_c2)
	(adjacent r4_c3 r4_c4)
	(adjacent r4_c3 r5_c3)
	(adjacent r4_c4 r3_c4)
	(adjacent r4_c4 r4_c3)
	(adjacent r4_c4 r4_c5)
	(adjacent r4_c4 r5_c4)
	(adjacent r4_c5 r3_c5)
	(adjacent r4_c5 r4_c4)
	(adjacent r4_c5 r4_c6)
	(adjacent r4_c5 r5_c5)
	(adjacent r4_c6 r3_c6)
	(adjacent r4_c6 r4_c5)
	(adjacent r4_c6 r4_c7)
	(adjacent r4_c6 r5_c6)
	(adjacent r4_c7 r3_c7)
	(adjacent r4_c7 r4_c6)
	(adjacent r4_c7 r4_c8)
	(adjacent r4_c7 r5_c7)
	(adjacent r4_c8 r3_c8)
	(adjacent r4_c8 r4_c7)
	(adjacent r4_c8 r4_c9)
	(adjacent r4_c8 r5_c8)
	(adjacent r4_c9 r3_c9)
	(adjacent r4_c9 r4_c10)
	(adjacent r4_c9 r4_c8)
	(adjacent r4_c9 r5_c9)
	(adjacent r5_c0 r4_c0)
	(adjacent r5_c0 r5_c1)
	(adjacent r5_c0 r6_c0)
	(adjacent r5_c10 r4_c10)
	(adjacent r5_c10 r5_c9)
	(adjacent r5_c10 r6_c10)
	(adjacent r5_c1 r4_c1)
	(adjacent r5_c1 r5_c0)
	(adjacent r5_c1 r5_c2)
	(adjacent r5_c1 r6_c1)
	(adjacent r5_c2 r4_c2)
	(adjacent r5_c2 r5_c1)
	(adjacent r5_c2 r5_c3)
	(adjacent r5_c2 r6_c2)
	(adjacent r5_c3 r4_c3)
	(adjacent r5_c3 r5_c2)
	(adjacent r5_c3 r5_c4)
	(adjacent r5_c3 r6_c3)
	(adjacent r5_c4 r4_c4)
	(adjacent r5_c4 r5_c3)
	(adjacent r5_c4 r5_c5)
	(adjacent r5_c4 r6_c4)
	(adjacent r5_c5 r4_c5)
	(adjacent r5_c5 r5_c4)
	(adjacent r5_c5 r5_c6)
	(adjacent r5_c5 r6_c5)
	(adjacent r5_c6 r4_c6)
	(adjacent r5_c6 r5_c5)
	(adjacent r5_c6 r5_c7)
	(adjacent r5_c6 r6_c6)
	(adjacent r5_c7 r4_c7)
	(adjacent r5_c7 r5_c6)
	(adjacent r5_c7 r5_c8)
	(adjacent r5_c7 r6_c7)
	(adjacent r5_c8 r4_c8)
	(adjacent r5_c8 r5_c7)
	(adjacent r5_c8 r5_c9)
	(adjacent r5_c8 r6_c8)
	(adjacent r5_c9 r4_c9)
	(adjacent r5_c9 r5_c10)
	(adjacent r5_c9 r5_c8)
	(adjacent r5_c9 r6_c9)
	(adjacent r6_c0 r5_c0)
	(adjacent r6_c0 r6_c1)
	(adjacent r6_c0 r7_c0)
	(adjacent r6_c10 r5_c10)
	(adjacent r6_c10 r6_c9)
	(adjacent r6_c10 r7_c10)
	(adjacent r6_c1 r5_c1)
	(adjacent r6_c1 r6_c0)
	(adjacent r6_c1 r6_c2)
	(adjacent r6_c1 r7_c1)
	(adjacent r6_c2 r5_c2)
	(adjacent r6_c2 r6_c1)
	(adjacent r6_c2 r6_c3)
	(adjacent r6_c2 r7_c2)
	(adjacent r6_c3 r5_c3)
	(adjacent r6_c3 r6_c2)
	(adjacent r6_c3 r6_c4)
	(adjacent r6_c3 r7_c3)
	(adjacent r6_c4 r5_c4)
	(adjacent r6_c4 r6_c3)
	(adjacent r6_c4 r6_c5)
	(adjacent r6_c4 r7_c4)
	(adjacent r6_c5 r5_c5)
	(adjacent r6_c5 r6_c4)
	(adjacent r6_c5 r6_c6)
	(adjacent r6_c5 r7_c5)
	(adjacent r6_c6 r5_c6)
	(adjacent r6_c6 r6_c5)
	(adjacent r6_c6 r6_c7)
	(adjacent r6_c6 r7_c6)
	(adjacent r6_c7 r5_c7)
	(adjacent r6_c7 r6_c6)
	(adjacent r6_c7 r6_c8)
	(adjacent r6_c7 r7_c7)
	(adjacent r6_c8 r5_c8)
	(adjacent r6_c8 r6_c7)
	(adjacent r6_c8 r6_c9)
	(adjacent r6_c8 r7_c8)
	(adjacent r6_c9 r5_c9)
	(adjacent r6_c9 r6_c10)
	(adjacent r6_c9 r6_c8)
	(adjacent r6_c9 r7_c9)
	(adjacent r7_c0 r6_c0)
	(adjacent r7_c0 r7_c1)
	(adjacent r7_c0 r8_c0)
	(adjacent r7_c10 r6_c10)
	(adjacent r7_c10 r7_c9)
	(adjacent r7_c10 r8_c10)
	(adjacent r7_c1 r6_c1)
	(adjacent r7_c1 r7_c0)
	(adjacent r7_c1 r7_c2)
	(adjacent r7_c1 r8_c1)
	(adjacent r7_c2 r6_c2)
	(adjacent r7_c2 r7_c1)
	(adjacent r7_c2 r7_c3)
	(adjacent r7_c2 r8_c2)
	(adjacent r7_c3 r6_c3)
	(adjacent r7_c3 r7_c2)
	(adjacent r7_c3 r7_c4)
	(adjacent r7_c3 r8_c3)
	(adjacent r7_c4 r6_c4)
	(adjacent r7_c4 r7_c3)
	(adjacent r7_c4 r7_c5)
	(adjacent r7_c4 r8_c4)
	(adjacent r7_c5 r6_c5)
	(adjacent r7_c5 r7_c4)
	(adjacent r7_c5 r7_c6)
	(adjacent r7_c5 r8_c5)
	(adjacent r7_c6 r6_c6)
	(adjacent r7_c6 r7_c5)
	(adjacent r7_c6 r7_c7)
	(adjacent r7_c6 r8_c6)
	(adjacent r7_c7 r6_c7)
	(adjacent r7_c7 r7_c6)
	(adjacent r7_c7 r7_c8)
	(adjacent r7_c7 r8_c7)
	(adjacent r7_c8 r6_c8)
	(adjacent r7_c8 r7_c7)
	(adjacent r7_c8 r7_c9)
	(adjacent r7_c8 r8_c8)
	(adjacent r7_c9 r6_c9)
	(adjacent r7_c9 r7_c10)
	(adjacent r7_c9 r7_c8)
	(adjacent r7_c9 r8_c9)
	(adjacent r8_c0 r7_c0)
	(adjacent r8_c0 r8_c1)
	(adjacent r8_c0 r9_c0)
	(adjacent r8_c10 r7_c10)
	(adjacent r8_c10 r8_c9)
	(adjacent r8_c10 r9_c10)
	(adjacent r8_c1 r7_c1)
	(adjacent r8_c1 r8_c0)
	(adjacent r8_c1 r8_c2)
	(adjacent r8_c1 r9_c1)
	(adjacent r8_c2 r7_c2)
	(adjacent r8_c2 r8_c1)
	(adjacent r8_c2 r8_c3)
	(adjacent r8_c2 r9_c2)
	(adjacent r8_c3 r7_c3)
	(adjacent r8_c3 r8_c2)
	(adjacent r8_c3 r8_c4)
	(adjacent r8_c3 r9_c3)
	(adjacent r8_c4 r7_c4)
	(adjacent r8_c4 r8_c3)
	(adjacent r8_c4 r8_c5)
	(adjacent r8_c4 r9_c4)
	(adjacent r8_c5 r7_c5)
	(adjacent r8_c5 r8_c4)
	(adjacent r8_c5 r8_c6)
	(adjacent r8_c5 r9_c5)
	(adjacent r8_c6 r7_c6)
	(adjacent r8_c6 r8_c5)
	(adjacent r8_c6 r8_c7)
	(adjacent r8_c6 r9_c6)
	(adjacent r8_c7 r7_c7)
	(adjacent r8_c7 r8_c6)
	(adjacent r8_c7 r8_c8)
	(adjacent r8_c7 r9_c7)
	(adjacent r8_c8 r7_c8)
	(adjacent r8_c8 r8_c7)
	(adjacent r8_c8 r8_c9)
	(adjacent r8_c8 r9_c8)
	(adjacent r8_c9 r7_c9)
	(adjacent r8_c9 r8_c10)
	(adjacent r8_c9 r8_c8)
	(adjacent r8_c9 r9_c9)
	(adjacent r9_c0 r10_c0)
	(adjacent r9_c0 r8_c0)
	(adjacent r9_c0 r9_c1)
	(adjacent r9_c10 r10_c10)
	(adjacent r9_c10 r8_c10)
	(adjacent r9_c10 r9_c9)
	(adjacent r9_c1 r10_c1)
	(adjacent r9_c1 r8_c1)
	(adjacent r9_c1 r9_c0)
	(adjacent r9_c1 r9_c2)
	(adjacent r9_c2 r10_c2)
	(adjacent r9_c2 r8_c2)
	(adjacent r9_c2 r9_c1)
	(adjacent r9_c2 r9_c3)
	(adjacent r9_c3 r10_c3)
	(adjacent r9_c3 r8_c3)
	(adjacent r9_c3 r9_c2)
	(adjacent r9_c3 r9_c4)
	(adjacent r9_c4 r10_c4)
	(adjacent r9_c4 r8_c4)
	(adjacent r9_c4 r9_c3)
	(adjacent r9_c4 r9_c5)
	(adjacent r9_c5 r10_c5)
	(adjacent r9_c5 r8_c5)
	(adjacent r9_c5 r9_c4)
	(adjacent r9_c5 r9_c6)
	(adjacent r9_c6 r10_c6)
	(adjacent r9_c6 r8_c6)
	(adjacent r9_c6 r9_c5)
	(adjacent r9_c6 r9_c7)
	(adjacent r9_c7 r10_c7)
	(adjacent r9_c7 r8_c7)
	(adjacent r9_c7 r9_c6)
	(adjacent r9_c7 r9_c8)
	(adjacent r9_c8 r10_c8)
	(adjacent r9_c8 r8_c8)
	(adjacent r9_c8 r9_c7)
	(adjacent r9_c8 r9_c9)
	(adjacent r9_c9 r10_c9)
	(adjacent r9_c9 r8_c9)
	(adjacent r9_c9 r9_c10)
	(adjacent r9_c9 r9_c8)
	(at r10_c4)
	(ishill r10_c7)
	(iswater r0_c10)
	(iswater r0_c1)
	(iswater r0_c2)
	(iswater r0_c5)
	(iswater r0_c7)
	(iswater r0_c9)
	(iswater r10_c0)
	(iswater r10_c10)
	(iswater r10_c3)
	(iswater r10_c8)
	(iswater r10_c9)
	(iswater r1_c0)
	(iswater r1_c10)
	(iswater r1_c9)
	(iswater r2_c7)
	(iswater r3_c1)
	(iswater r3_c8)
	(iswater r4_c2)
	(iswater r4_c3)
	(iswater r4_c4)
	(iswater r5_c4)
	(iswater r5_c8)
	(iswater r5_c9)
	(iswater r6_c3)
	(iswater r6_c6)
	(iswater r6_c7)
	(iswater r7_c0)
	(iswater r7_c7)
	(iswater r9_c10)
	(iswater r9_c1)
	(iswater r9_c3)
	(iswater r9_c6)
	(iswater r9_c9)
	(ontrail r10_c4 r10_c5)
	(ontrail r10_c5 r10_c6)
	(ontrail r10_c6 r10_c7)
	(ontrail r10_c7 r9_c7)
	(ontrail r1_c5 r1_c6)
	(ontrail r1_c6 r1_c7)
	(ontrail r1_c7 r1_c8)
	(ontrail r2_c0 r2_c1)
	(ontrail r2_c1 r2_c2)
	(ontrail r2_c2 r3_c2)
	(ontrail r2_c5 r1_c5)
	(ontrail r3_c0 r2_c0)
	(ontrail r3_c2 r3_c3)
	(ontrail r3_c3 r3_c4)
	(ontrail r3_c4 r3_c5)
	(ontrail r3_c5 r2_c5)
	(ontrail r4_c0 r3_c0)
	(ontrail r4_c10 r4_c9)
	(ontrail r4_c7 r5_c7)
	(ontrail r4_c8 r4_c7)
	(ontrail r4_c9 r4_c8)
	(ontrail r5_c0 r4_c0)
	(ontrail r5_c10 r4_c10)
	(ontrail r5_c1 r5_c0)
	(ontrail r5_c5 r6_c5)
	(ontrail r5_c6 r5_c5)
	(ontrail r5_c7 r5_c6)
	(ontrail r6_c10 r5_c10)
	(ontrail r6_c1 r5_c1)
	(ontrail r6_c2 r6_c1)
	(ontrail r6_c5 r7_c5)
	(ontrail r7_c10 r6_c10)
	(ontrail r7_c2 r6_c2)
	(ontrail r7_c3 r7_c2)
	(ontrail r7_c5 r8_c5)
	(ontrail r7_c9 r7_c10)
	(ontrail r8_c3 r7_c3)
	(ontrail r8_c4 r8_c3)
	(ontrail r8_c5 r8_c4)
	(ontrail r8_c7 r8_c8)
	(ontrail r8_c8 r8_c9)
	(ontrail r8_c9 r7_c9)
	(ontrail r9_c7 r8_c7)
  )
  (:goal (and
	(at r1_c8)))
)

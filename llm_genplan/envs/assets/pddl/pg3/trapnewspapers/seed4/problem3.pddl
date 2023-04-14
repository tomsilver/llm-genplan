
(define (problem newspaper) (:domain trapnewspapers)
  (:objects
        loc-0 - loc
	loc-1 - loc
	loc-2 - loc
	loc-3 - loc
	loc-4 - loc
	loc-5 - loc
	loc-6 - loc
	paper-0 - paper
	paper-1 - paper
  )
  (:init 
	(at loc-0)
	(ishomebase loc-0)
	(safe loc-0)
	(safe loc-3)
	(safe loc-5)
	(unpacked paper-0)
	(unpacked paper-1)
	(wantspaper loc-3)
	(wantspaper loc-5)
  )
  (:goal (and
	(satisfied loc-3)
	(satisfied loc-5)))
)


(define (problem my-problem-1) (:domain my-pddl-domain)
  (:objects
        object0 - type0
	object1 - type0
	object2 - type0
	object3 - type0
	object4 - type0
	object5 - type1
	object6 - type1
	object7 - type1
  )
  (:init 
	(predicate0 object0)
	(predicate3 object0)
	(predicate6 object0)
	(predicate6 object1)
	(predicate6 object3)
	(predicate6 object4)
	(predicate8 object5)
	(predicate8 object6)
	(predicate8 object7)
	(predicate9 object1)
	(predicate9 object3)
	(predicate9 object4)
  )
  (:goal (and
	(predicate7 object1)
	(predicate7 object3)
	(predicate7 object4)))
)

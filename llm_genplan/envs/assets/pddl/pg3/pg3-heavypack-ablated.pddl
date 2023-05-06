(define (domain my-pddl-domain)
   (:predicates
		(predicate1 ?v2 ?v3)
        (predicate4 ?v1)
        (predicate6 ?v1)
        (predicate2 ?v1)
        (predicate0)
	)

   (:action operator0
       :parameters (?v1)
       :precondition (and (predicate0))
       :effect (and (not (predicate0)) (predicate4 ?v1) (predicate2 ?v1) (not (predicate6 ?v1))))

   (:action operator1
       :parameters (?v0 ?v4)
       :precondition (and (predicate4 ?v0) (predicate2 ?v0) (predicate1 ?v0 ?v4) (predicate6 ?v4))
       :effect (and (predicate4 ?v4) (predicate2 ?v4) (not (predicate2 ?v0)) (not (predicate6 ?v4))))
)

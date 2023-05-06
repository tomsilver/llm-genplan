(define (domain my-pddl-domain)
   (:predicates (predicate9 ?v6)
		(predicate2 ?v0)
		(predicate6 ?v2)
		(predicate1 ?v6)
		(predicate0 ?v0 ?v6)
		(predicate5 ?v2)
		(predicate3 ?v4 ?v2))

   (:action operator1
       :parameters  (?v1 ?v8)
       :precondition (and  (predicate9 ?v1) (predicate9 ?v8) (predicate1 ?v1))
       :effect (and  (predicate1 ?v8)
		     (not (predicate1 ?v1))))



   (:action operator2
       :parameters (?v5 ?v7 ?v3)
       :precondition  (and  (predicate2 ?v5) (predicate9 ?v7) (predicate6 ?v3)
			    (predicate0 ?v5 ?v7) (predicate1 ?v7) (predicate5 ?v3))
       :effect (and (predicate3 ?v5 ?v3)
		    (not (predicate0 ?v5 ?v7)) 
		    (not (predicate5 ?v3))))


   (:action operator0
       :parameters  (?v5  ?v7 ?v3)
       :precondition  (and  (predicate2 ?v5) (predicate9 ?v7) (predicate6 ?v3)
			    (predicate3 ?v5 ?v3) (predicate1 ?v7))
       :effect (and (predicate0 ?v5 ?v7)
		    (predicate5 ?v3)
		    (not (predicate3 ?v5 ?v3)))))

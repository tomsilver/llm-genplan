(define (domain my-pddl-domain)
   (:predicates (predicate7 ?v6 ?v7)
        (predicate3 ?v0)
        (predicate6 ?v3)
        (predicate1 ?v3)
        (predicate0 ?v0 ?v3)
        (predicate5)
        (predicate8 ?v0))

   (:action operator2
       :parameters  (?v2 ?v5)
       :precondition (and (predicate7 ?v2 ?v5) 
                          (predicate6 ?v2) (predicate6 ?v5) (predicate1 ?v2))
       :effect (and  (predicate1 ?v5)
             (not (predicate1 ?v2))))


   (:action operator0
       :parameters (?v1 ?v4)
       :precondition  (and  (predicate3 ?v1) (predicate6 ?v4)
                (predicate0 ?v1 ?v4) (predicate1 ?v4) (predicate5))
       :effect (and (predicate8 ?v1)
            (not (predicate0 ?v1 ?v4)) 
            (not (predicate5))))

   (:action operator1
       :parameters  (?v1  ?v4)
       :precondition  (and  (predicate3 ?v1) (predicate6 ?v4)
                (predicate8 ?v1) (predicate1 ?v4))
       :effect (and (predicate0 ?v1 ?v4)
            (predicate5)
            (not (predicate8 ?v1)))))
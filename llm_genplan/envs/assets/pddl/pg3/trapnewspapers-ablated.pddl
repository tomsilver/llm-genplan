(define (domain my-pddl-domain)
    (:requirements :strips :typing)
    (:types type0 type1)
    (:predicates 
        (predicate0 ?v1 - type0)
        (predicate3 ?v1 - type0)
        (predicate7 ?v1 - type0)
        (predicate9 ?v1 - type0)
        (predicate6 ?v1 - type0)
        (predicate8 ?v2 - type1)
        (predicate1 ?v2 - type1)
    )
    
    (:action operator2
        :parameters (?v2 - type1 ?v1 - type0)
        :precondition (and
            (predicate0 ?v1)
            (predicate3 ?v1)
            (predicate8 ?v2)
        )
        :effect (and
            (not (predicate8 ?v2))
            (predicate1 ?v2)
        )
    )
    
    (:action operator1
        :parameters (?v0 - type0 ?v3 - type0)
        :precondition (and
            (predicate0 ?v0)
            (predicate6 ?v0)
        )
        :effect (and
            (not (predicate0 ?v0))
            (predicate0 ?v3)
        )
    )
    
    (:action operator0
        :parameters (?v2 - type1 ?v1 - type0)
        :precondition (and
            (predicate0 ?v1)
            (predicate1 ?v2)
        )
        :effect (and
            (not (predicate1 ?v2))
            (not (predicate9 ?v1))
            (predicate7 ?v1)
        )
    )
    
)
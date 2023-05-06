(define (domain my-pddl-domain)
  (:requirements :strips)
  (:types type2 - type1
          type0 - type1
  )

(:predicates
(predicate7 ?v7 - type2 ?v3 - type0)
(predicate4 ?v7 - type2 ?v3 - type0)
(predicate0 ?v4 - type0  ?v5 - type0)
(predicate2 ?v7 - type2)
(predicate8 ?v7 - type2)
(predicate6 ?v3 - type0)
)

(:action operator0
  :parameters (?v0 - type0 ?v6 - type2)
  :precondition (and (predicate6 ?v0)
                     (predicate7 ?v6 ?v0)
                )
  :effect (and (predicate2 ?v6)
          )
)

(:action operator1
  :parameters (?v0 - type0 ?v6 - type2)
  :precondition (and (predicate6 ?v0)
                     (predicate4 ?v6 ?v0)
                     (predicate2 ?v6)
                )
  :effect (and (not (predicate2 ?v6))
               (predicate8 ?v6)
          )
)

(:action operator3
  :parameters (?v1 - type0 ?v2 - type0)
  :precondition (and (predicate6 ?v1)
                     (predicate0 ?v1 ?v2)
                )
  :effect (and (predicate6 ?v2)
               (not (predicate6 ?v1))
          )
)

(:action operator2
  :parameters (?v1 - type0 ?v2 - type0)
  :precondition (and (predicate6 ?v1)
                     (predicate0 ?v2 ?v1)
                )
  :effect (and (predicate6 ?v2)
               (not (predicate6 ?v1))
          )
)
)
(define (domain my-pddl-domain)
  (:requirements :strips :typing)
  (:types type0)

(:predicates
  (predicate1 ?v1 - type0)
  (predicate4 ?v1 - type0)
  (predicate3 ?v1 - type0)
  (predicate0 ?v2 - type0 ?v3 - type0)
  (predicate5 ?v0 - type0 ?v4 - type0)
)

(:action operator1
  :parameters (?v0 - type0 ?v4 - type0)
  :precondition (and
    (not (predicate3 ?v4))
    (predicate1 ?v0)
    (predicate0 ?v0 ?v4)
    (not (predicate4 ?v0)))
  :effect (and (predicate1 ?v4) (not (predicate1 ?v0)))
)

(:action operator0
  :parameters (?v0 - type0 ?v4 - type0)
  :precondition (and
    (predicate3 ?v4)
    (predicate1 ?v0)
    (predicate0 ?v0 ?v4)
    (not (predicate4 ?v0)))
  :effect (and (predicate1 ?v4) (not (predicate1 ?v0)))
)


)

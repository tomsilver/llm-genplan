(define (problem my-problem-8)
 (:domain my-pddl-domain)
 (:objects 
     object0 - type3
 object9 object10 object11 - type6
     object5 object6 object7 - type4
     object2 object3 object4 - type2
     object8 object1 - type2
    )
 (:init 
    (predicate0 object0 object8)
    (predicate0 object9 object2)
    (predicate7 object9)
    (predicate0 object10 object2)
    (predicate7 object10)
    (predicate0 object11 object4)
    (predicate7 object11)
    (predicate3 object5)
    (predicate0 object5 object1)
    (predicate3 object6)
    (predicate0 object6 object1)
    (predicate3 object7)
    (predicate0 object7 object1)
    (predicate2 object8 object2)
    (predicate2 object4 object1)
    (predicate2 object2 object3)
    (predicate2 object3 object4)
)
 (:goal
  (and
   (predicate6 object5)
   (predicate6 object6)
   (predicate6 object7)
)))
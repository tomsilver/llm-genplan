(define (problem my-problem-4)
 (:domain my-pddl-domain)
 (:objects 
     object0 - type3
 object10 object11 object12 object13 - type6
     object6 object7 object8 - type4
     object2 object3 object4 object5 - type2
     object9 object1 - type2
    )
 (:init 
    (predicate0 object0 object9)
    (predicate0 object10 object5)
    (predicate7 object10)
    (predicate0 object11 object5)
    (predicate7 object11)
    (predicate0 object12 object5)
    (predicate7 object12)
    (predicate0 object13 object5)
    (predicate7 object13)
    (predicate3 object6)
    (predicate0 object6 object1)
    (predicate3 object7)
    (predicate0 object7 object1)
    (predicate3 object8)
    (predicate0 object8 object1)
    (predicate2 object9 object2)
    (predicate2 object5 object1)
    (predicate2 object2 object3)
    (predicate2 object3 object4)
    (predicate2 object4 object5)
)
 (:goal
  (and
   (predicate6 object6)
   (predicate6 object7)
   (predicate6 object8)
)))
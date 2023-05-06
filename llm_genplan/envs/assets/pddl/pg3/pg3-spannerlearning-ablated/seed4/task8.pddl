(define (problem my-problem-8)
 (:domain my-pddl-domain)
 (:objects 
     object0 - type3
 object12 object13 object14 object15 object16 - type6
     object7 object8 object9 object10 - type4
     object2 object3 object4 object5 object6 - type2
     object11 object1 - type2
    )
 (:init 
    (predicate0 object0 object11)
    (predicate0 object12 object5)
    (predicate7 object12)
    (predicate0 object13 object6)
    (predicate7 object13)
    (predicate0 object14 object4)
    (predicate7 object14)
    (predicate0 object15 object2)
    (predicate7 object15)
    (predicate0 object16 object3)
    (predicate7 object16)
    (predicate3 object7)
    (predicate0 object7 object1)
    (predicate3 object8)
    (predicate0 object8 object1)
    (predicate3 object9)
    (predicate0 object9 object1)
    (predicate3 object10)
    (predicate0 object10 object1)
    (predicate2 object11 object2)
    (predicate2 object6 object1)
    (predicate2 object2 object3)
    (predicate2 object3 object4)
    (predicate2 object4 object5)
    (predicate2 object5 object6)
)
 (:goal
  (and
   (predicate6 object7)
   (predicate6 object8)
   (predicate6 object9)
   (predicate6 object10)
)))
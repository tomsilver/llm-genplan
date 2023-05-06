(define (domain my-pddl-domain)                    
(:requirements :typing :strips)                
(:types 
	type2 type0 - type5
	type3 type4 type6 - type0	
)                                           
                                                                               
(:predicates 
	(predicate0 ?v4 - type0 ?v1 - type2)
	(predicate1 ?v4 - type3 ?v6 - type6)
	(predicate7 ?v6 - type6)
	(predicate2 ?v2 - type2 ?v3 - type2)
	(predicate6 ?v5 - type4)
	(predicate3 ?v5 - type4))                                                                                           

(:action operator2 
        :parameters (?v7 - type2 ?v0 - type2 ?v4 - type3)
        :precondition (and (predicate0 ?v4 ?v7) 
                           (predicate2 ?v7 ?v0))                                                          
        :effect (and (not (predicate0 ?v4 ?v7)) (predicate0 ?v4 ?v0)))

(:action operator0 
        :parameters (?v1 - type2 ?v6 - type6 ?v4 - type3)
        :precondition (and (predicate0 ?v4 ?v1) 
                           (predicate0 ?v6 ?v1))
        :effect (and (not (predicate0 ?v6 ?v1))
                     (predicate1 ?v4 ?v6)))

(:action operator1 
        :parameters (?v1 - type2 ?v6 - type6 ?v4 - type3 ?v5 - type4)
        :precondition (and (predicate0 ?v4 ?v1) 
		      	   (predicate0 ?v5 ?v1)
			   (predicate1 ?v4 ?v6)
			   (predicate7 ?v6)
			   (predicate3 ?v5))
        :effect (and (not (predicate3 ?v5))(not (predicate7 ?v6)) (predicate6 ?v5)))
)
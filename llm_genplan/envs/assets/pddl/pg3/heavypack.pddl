(define (domain heavy-pack)
   (:predicates
		(heavier ?item1 ?item2)
        (packed ?item)
        (unpacked ?item)
        (nothing-above ?item)
        (box-empty)
	)

   (:action pack-first
       :parameters (?item)
       :precondition (and (box-empty))
       :effect (and (not (box-empty)) (packed ?item) (nothing-above ?item) (not (unpacked ?item))))

   (:action stack
       :parameters (?bottom ?top)
       :precondition (and (packed ?bottom) (nothing-above ?bottom) (heavier ?bottom ?top) (unpacked ?top))
       :effect (and (packed ?top) (nothing-above ?top) (not (nothing-above ?bottom)) (not (unpacked ?top))))
)

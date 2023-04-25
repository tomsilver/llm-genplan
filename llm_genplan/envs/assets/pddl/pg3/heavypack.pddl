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
       :parameters (?item1 ?item2)
       :precondition (and (packed ?item1) (nothing-above ?item1) (heavier ?item1 ?item2) (unpacked ?item2))
       :effect (and (packed ?item2) (nothing-above ?item2) (not (nothing-above ?item1)) (not (unpacked ?item2))))
)

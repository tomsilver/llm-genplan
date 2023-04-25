(define (domain track-building)
   (:predicates
		(agent-at ?loc)
		(train-at ?loc)
		(has-track ?loc)
        (forward ?loc1 ?loc2)
	)

   (:action build-track
       :parameters  (?loc)
       :precondition (and (agent-at ?loc))
       :effect (and  (has-track ?loc)))

   (:action move-agent
       :parameters (?current-loc ?next-loc)
       :precondition (and (agent-at ?current-loc))
       :effect (and  (agent-at ?next-loc) (not (agent-at ?current-loc))))

   (:action move-train
       :parameters  (?current-loc ?next-loc)
       :precondition (and (train-at ?current-loc) (has-track ?next-loc)
                          (forward ?current-loc ?next-loc))
       :effect (and  (train-at ?next-loc) (not (train-at ?current-loc))))
)

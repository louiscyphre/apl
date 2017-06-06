(define (domain knights-tour)

  (:requirements :strips)
  
  (:predicates (NEIGHBOUR ?x ?y)
	       (knight-at ?x)
	       (visited ?x)
  )
  
  (:action move
    :parameters (?from ?to)
    :precondition
      (and
        (knight-at ?from)
        (NEIGHBOUR ?from ?to)
        (not (visited ?to))
      )
    :effect
      (and
        (not (knight-at ?from))
        (knight-at ?to)
        (visited ?to)
      )
  )
)

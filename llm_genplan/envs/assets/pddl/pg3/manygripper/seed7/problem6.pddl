
(define (problem manygripper) (:domain gripper-strips)
  (:objects
        ball0
	ball1
	ball2
	ball3
	ball4
	ball5
	gripper0
	gripper1
	room0
	room1
	room10
	room11
	room12
	room13
	room14
	room15
	room16
	room17
	room18
	room2
	room3
	room4
	room5
	room6
	room7
	room8
	room9
  )
  (:init 
	(at ball0 room9)
	(at ball1 room8)
	(at ball2 room15)
	(at ball3 room5)
	(at ball4 room9)
	(at ball5 room4)
	(at-robby room0)
	(ball ball0)
	(ball ball1)
	(ball ball2)
	(ball ball3)
	(ball ball4)
	(ball ball5)
	(free gripper0)
	(free gripper1)
	(gripper gripper0)
	(gripper gripper1)
	(room room0)
	(room room10)
	(room room11)
	(room room12)
	(room room13)
	(room room14)
	(room room15)
	(room room16)
	(room room17)
	(room room18)
	(room room1)
	(room room2)
	(room room3)
	(room room4)
	(room room5)
	(room room6)
	(room room7)
	(room room8)
	(room room9)
  )
  (:goal (and
	(at ball5 room1)
	(at ball0 room11)
	(at ball2 room12)
	(at ball3 room12)
	(at ball1 room13)))
)

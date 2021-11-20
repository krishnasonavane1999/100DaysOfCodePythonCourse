def turn_right():
    turn_left()
    turn_left()
    turn_left()
    

def specific_moves():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
    
while not at_goal():
    specific_moves()

    


def turn_right():
    turn_left()
    turn_left()
    turn_left()


def jump_wall():
    cnt_moves = 0
    turn_left()
    if wall_on_right():
        while wall_on_right():
            move()
            cnt_moves += 1
    turn_right()
    move()
    turn_right()
    while cnt_moves:
        move()
        cnt_moves -= 1
    turn_left()
while not at_goal():
    
    if wall_in_front():
       jump_wall()
        
    else:
        move()
        
    


    



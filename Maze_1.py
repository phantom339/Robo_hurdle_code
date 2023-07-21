def turn_right():
    turn_left()
    turn_left()
    turn_left()
def check_s():
    while front_is_clear():
        move()
    while wall_in_front():
        if right_is_clear():
            turn_right()
        elif not right_is_clear():
            turn_left()
    move()        
while not at_goal():
       check_s()
    
    
        








    
################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################

def turn_right():
    turn_left()
    turn_left()
    turn_left()
def hurdle():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
while at_goal() != True:
    while front_is_clear():
        move()
    while wall_in_front():
        hurdle()
        turn_left()








    
################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################

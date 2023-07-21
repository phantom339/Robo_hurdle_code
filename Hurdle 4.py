def turn_right():
    turn_left()
    turn_left()
    turn_left()
def jump():
    hei=1
    while wall_in_front():
        turn_left()
        move()
        while wall_on_right():
            move()
            hei+=1
        turn_right()
        move()
        turn_right()
        for i in range(0,hei):
            if not wall_in_front():
                move() 
        turn_left()       
while at_goal() != True:
    while front_is_clear() and not at_goal():
        move()
    while wall_in_front():
        jump()
        








    
################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################

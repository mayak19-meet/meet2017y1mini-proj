import turtle
import random
turtle.tracer(1,0)
size_x=800
size_y=500

turtle.setup(size_x,size_y)
turtle.penup()

square_size=20
start_length=7

pos_list=[]
stamp_list=[]
food_pos=[]
food_stamps=[]

snake=turtle.clone()
snake.shape("square")
turtle.hideturtle()

for i in range(start_length):
    x_pos=snake.pos()[0]
    y_pos=snake.pos()[1]

    x_pos+=square_size
    
    my_pos=(x_pos,y_pos)
    snake.goto(x_pos,y_pos)
    
    pos_list.append(my_pos)

    snake1=snake.stamp()
    stamp_list.append(snake1)

UP_ARROW="Up"
LEFT_ARROW="Left"
DOWN_ARROW="Down"
RIGHT_ARROW="Right"
TIME_STEP=100
SPACEBAR="space"

UP=0
DOWN=1
LETF=2
RIGHT=3


direction=UP
def up ():
    global direction
    direction=UP
    move_snake()
    print("you pressed the up key!")


#direction=down
def down ():
    global direction
    direction=DOWN
    move_snake()
    print("you pressed the down key!")


#direction=LEFT
def left ():
    global direction
    direction=LEFT
    move_snake()
    print("you pressed the left key!")



#direction=RIGHT
def right ():
    global direction
    direction=RIGHT
    move_snake()
    print("you pressed the right key!")





turtle.onkeypress(up,UP_ARROW)
turtle.onkeypress(down ,DOWN_ARROW)
turtle.onkeypress(left,LEFT_ARROW)
turtle.onkeypress(right,RIGHT_ARROW)


turtle.listen()
def move_snake():
    my_pos=snake.pos()
    x_pos=my_pos[0]
    y_pos=my_pos[1]


    if direction==RIGHT:
        snake.goto(x_pos+square_size,y_pos)
        print("you moved right!")
    elif direction==LEFT:
        snake.goto(x_pos-square_size,y_pos)
        print("you moved leftt!")

    if direction==UP:
        snake.goto(x_pos+square_size,y_pos)
        print("you moved up!")
    elif direction==DOWN:
        snake.goto(x_pos-square_size,y_pos)
        print("you moved down!")


    














    
    
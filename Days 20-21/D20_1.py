#Building the snake game
from turtle import Turtle, Screen
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

segments = []
x_pos = [0, -20, -40]

for i in range(0, 3): 
    new_segment = Turtle(shape='square')
    new_segment.penup()
    new_segment.color("white")
    new_segment.setpos(x= x_pos[i], y=0)
    segments.append(new_segment)
 

    
game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    for seg in range(len(segments)-1, 0, -1):
        new_x = segments[seg - 1].xcor()
        new_y = segments[seg - 1].ycor()
        segments[seg].goto(new_x, new_y)
    segments[0].fd(20)     
        

screen.listen()
'''
screen.onkey(key= "Up", fun=move_forwards)
screen.onkey(key= "Down", fun=move_backwards)
screen.onkey(key= "Left", fun=turn_left)
screen.onkey(key= "Right", fun=turn_right)
screen.onkey(key= "c", fun=clear)
'''

screen.exitonclick()
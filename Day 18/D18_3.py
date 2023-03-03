from turtle import Turtle, Screen
import random 

tColors = ["red", "black", "green", "blue", "pink", "yellow", "brown", "grey"]
col = random.choice(tColors) 

donatello = Turtle()
donatello.shape("turtle")  
 
def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        donatello.fd(100)
        donatello.right(angle)

for n in range(3, 11):
    draw_shape(n)
    donatello.color(random.choice(tColors))

screen = Screen()
screen.exitonclick()
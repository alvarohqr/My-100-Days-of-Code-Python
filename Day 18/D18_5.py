import turtle as t
from turtle import Screen
import random 

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rColor = (r, g, b)
    return rColor
    
tDirection = [0, 90, 180, 270]

donatello = t.Turtle()  
donatello.pensize(15)
donatello.speed(10)
t.colormode(255)

for _ in range(200):
    donatello.color((random_color()))
    donatello.fd(30)
    donatello.setheading(random.choice(tDirection))

screen = Screen()
screen.exitonclick()
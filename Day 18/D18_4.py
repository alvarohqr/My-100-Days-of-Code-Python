from turtle import Turtle, Screen
import random 

tColors = ["red", "black", "green", "blue", "pink", "yellow", "brown", "grey"]
col = random.choice(tColors) 

tDirection = [0, 90, 180, 270]

donatello = Turtle()  
donatello.pensize(15)
donatello.speed(10)

for _ in range(200):
    donatello.color(random.choice(tColors))
    donatello.fd(30)
    donatello.setheading(random.choice(tDirection))

screen = Screen()
screen.exitonclick()
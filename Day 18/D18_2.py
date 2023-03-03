from turtle import Turtle, Screen

donatello = Turtle()

for _ in range(20):
    donatello.fd(10)
    donatello.pu()
    donatello.fd(10)
    donatello.pd()
    
screen = Screen()
screen.exitonclick()
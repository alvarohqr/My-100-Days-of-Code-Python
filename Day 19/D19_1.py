from turtle import Turtle, Screen

donatello = Turtle()

screen = Screen()

def move_forwards():
    donatello.fd(10)
    
screen.listen()
screen.onkey(key= "space", fun=move_forwards)
screen.exitonclick()
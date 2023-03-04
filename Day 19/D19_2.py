from turtle import Turtle, Screen

donatello = Turtle()

screen = Screen()

def move_forwards():
    donatello.fd(10)

def move_backwards():
    donatello.backward(10)
    
def turn_left():
    donatello.setheading(donatello.heading() + 10)

def turn_right():
    donatello.setheading(donatello.heading() - 10)

def clear():
    donatello.clear()
    donatello.home()
    screen.clear()

screen.listen()
screen.onkey(key= "w", fun=move_forwards)
screen.onkey(key= "s", fun=move_backwards)
screen.onkey(key= "a", fun=turn_left)
screen.onkey(key= "d", fun=turn_right)
screen.onkey(key= "c", fun=clear)
screen.exitonclick()
from turtle import Turtle, Screen

l = int(input("Square lenght: "))
donatello = Turtle()
donatello.shape("turtle") 
donatello.color("green")

def turtle_square(l):
    '''The turtle draws a square'''
    for _ in range(4):
        donatello.forward(l)
        donatello.left(90)  

turtle_square(l)
screen = Screen()
screen.exitonclick()
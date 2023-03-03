import turtle as t 
import random 

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rColor = (r, g, b)
    return rColor
    
tDirection = [0, 90, 180, 270]

donatello = t.Turtle()   
t.colormode(255) 
donatello.speed("fastest")


def draw_spiro(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        donatello.color(random_color())
        donatello.circle(180)
        donatello.setheading(donatello.heading() + size_of_gap)

draw_spiro(5)

screen = t.Screen()
screen.exitonclick()
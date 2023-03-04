from turtle import Turtle, Screen
import random


'''
rafael = Turtle()
michaelangelo = Turtle()
leonardo = Turtle()
'''

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
all_turtles = []
colors = ["purple", "red", "orange", "blue"]
y_pos = [150, 50, -50, -150]

for i in range(0, 4): 
    new_turtle = Turtle(shape='turtle')
    new_turtle.penup() 
    new_turtle.color(colors[i])
    new_turtle.setpos(-240, y_pos[i])   
    new_turtle.speed("fastest")
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner")
            
        rand_dist = random.randint(0, 10)
        turtle.fd(rand_dist)

'''
rafael.color("red")
rafael.penup()
rafael.shape("turtle")
rafael.setpos(-240, 50)

michaelangelo.color("orange")
michaelangelo.penup()
michaelangelo.shape("turtle")
michaelangelo.setpos(-240, -50)

leonardo.color("blue")
leonardo.penup()
leonardo.shape("turtle")
leonardo.setpos(-240, -150)
'''




screen.exitonclick()
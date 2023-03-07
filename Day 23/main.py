from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("PONG")
screen.tracer(0)

Rpaddle = Paddle((350,0))
Lpaddle = Paddle((-350,0))
game_is_on = True

ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(Rpaddle.go_down, "Down")
screen.onkey(Rpaddle.go_up, "Up")
screen.onkey(Lpaddle.go_down, "s")
screen.onkey(Lpaddle.go_up, "w")

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    
    #Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.wall_bounce() 

    #Detec collision with paddle
    if ball.distance(Rpaddle) < 50 and ball.xcor() > 320 or ball.distance(Lpaddle) < 50 and ball.xcor() < -320:
        ball.paddle_bounce()
        
    #Detect if R paddle miss it
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()
        
    #Detect if R paddle miss it
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()
        
screen.exitonclick()
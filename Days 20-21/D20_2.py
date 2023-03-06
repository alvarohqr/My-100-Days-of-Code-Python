#Building the snake game
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)


snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1) 
    snake.move()
        
    #Detect collision with food
    if snake.head.distance(food) < 15:  
        food.refresh()
        snake.extend()
        scoreboard.increase_score()
    #Detect collision with wall
    xcord = snake.head.xcor()
    ycord = snake.head.ycor()
    if xcord > 280 or xcord < -280 or ycord > 280 or ycord < -280:
        game_is_on = False
        #screen.clear()
        #screen.bgcolor("black")
        scoreboard.game_over()
    #Detect collision with tail
    for segment in snake.snakes[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()


screen.exitonclick()
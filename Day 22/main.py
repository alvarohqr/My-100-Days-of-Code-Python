import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)


player = Player()
car = CarManager()

screen.listen()
screen.onkey(player.go_up, "Up")
score = Scoreboard()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.create_cars()
    car.move_cars()
    
    #Detect collision with car
    for _car in car.all_cars:
        if _car.distance(player) < 25:
            score.game_over()
            game_is_on = False
            
    #Detect when the turtle reach the other side
    if player.ycor() > 280:
        player.start()
        car.level_up() 
        score.update_score()

screen.exitonclick()
from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.color("black")
        self.start()
        
    def go_up(self):
        self.fd(MOVE_DISTANCE)
        
    def start(self):
        self.setpos(STARTING_POSITION)
        self.setheading(90)

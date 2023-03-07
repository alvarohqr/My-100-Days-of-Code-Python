from turtle import Turtle

class Ball(Turtle):
    def __init__(self, shape: str = "circle", undobuffersize: int = 1000, visible: bool = True) -> None:
        super().__init__(shape, undobuffersize, visible)  
        self.color("white")                                       
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1
        
    def move(self):
        xcor = self.xcor() + self.x_move 
        ycor = self.ycor() + self.y_move
        self.goto(x=xcor, y=ycor)
        
    def wall_bounce(self):
        self.y_move *= -1 
    
    def paddle_bounce(self):
        self.x_move *= -1 
        self.move_speed *= 0.9

    def reset_position(self):
        self.home()
        self.move_speed = 0.1
        self.paddle_bounce()
        
        
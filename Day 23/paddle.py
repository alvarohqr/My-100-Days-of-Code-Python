from turtle import Turtle

WIDTH   =   5
HEIGHT  =   1

class Paddle(Turtle):
    def __init__(self, position) -> None:
        super().__init__()
        self.shape("square")
        self.penup()
        self.color("white")
        self.shapesize(stretch_len=HEIGHT, stretch_wid= WIDTH)
        self.setpos(position)
        
    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(x=self.xcor(), y=new_y)
        
    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(x=self.xcor(), y=new_y)        
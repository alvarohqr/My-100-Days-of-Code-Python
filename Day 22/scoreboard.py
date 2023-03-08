from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.penup()
        self.ht()
        self.level = 1
        self.penup()
        self.color("black")
        self.score()
        
    def score(self):
        self.clear()
        self.setpos(-280, 260)
        self.write(f"Level = {self.level}",  align= "left", font=FONT) 
        
    def update_score(self):
        self.level += 1
        self.score()
    
    def game_over(self):
        self.home()
        self.write("GAME OVER", align="center", font=FONT)

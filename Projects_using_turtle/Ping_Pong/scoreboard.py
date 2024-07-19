
from turtle import Turtle

class Scoreboard(Turtle):
    
    def __init__(self):
        
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l = 0
        self.r = 0
        self.update_scoreboard()
        
    def update_scoreboard(self):
        self.goto(-100,180)
        self.write(self.l,align="center",font=("Courier",80,"normal"))
        self.goto(100,180)
        self.write(self.r,align="center",font=("Courier",80,"normal"))
                
    def l_point(self):
        self.clear()
        self.l += 1   
        self.update_scoreboard()
        
    def r_point(self):
        self.clear()
        self.r += 1
        self.update_scoreboard()

from turtle import Turtle

class Ball(Turtle):
    
    def __init__(self):
        
        super().__init__()
        
        self.shape("circle")
        self.width(20)
        self.color("white")
        self.penup()
        self.X = 10
        self.Y = 10
        self.move_speed = 0.1
        
    def move(self):
        self.goto(self.xcor() + self.X , self.ycor() + self.Y)
    
    def bounce_y(self): 
        self.Y *= -1
        
    def bounce_x(self):
        self.X *= -1
        self.move_speed *= 0.9
        
        
    def reset_position(self):
        self.move_speed = 0.1
        self.goto(0,0)
        self.bounce_x()
        
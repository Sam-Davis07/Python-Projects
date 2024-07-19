
from turtle import Turtle

class Paddle(Turtle):
        
        def __init__(self,X,Y):
                
                super().__init__()
                self.color("white")
                self.shape("square")
                self.shapesize(stretch_len=1,stretch_wid=5)
                self.penup()
                self.goto(X,Y)
        
        def goUp(self):
                self.goto(self.xcor() , self.ycor() + 20)

        def goDown(self):
                self.goto(self.xcor() , self.ycor() - 20)


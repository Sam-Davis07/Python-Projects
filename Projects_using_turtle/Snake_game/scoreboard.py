from turtle import Turtle

FONT = ("Arial",24,"normal")
ALIGNMENT = "center"

class Scoreboard(Turtle):
    
    def __init__(self):
        
        super().__init__()
        with open("data.txt") as file:
            self.high_Score = int(file.read())
        self.score = 0
        self.color("white")
        self.goto(0,260)
        self.penup()
        self.hideturtle()
        self.update_scoreboard()
        
        
    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_Score}",align = ALIGNMENT ,font = FONT)
    
    def game_over(self):
        self.clear()
        self.goto(0,0)
        self.color("white")
        self.write(f"High Score: {self.high_Score}\nGAME OVER", align = ALIGNMENT , font = FONT)       


    def reset(self):
        if self.score > self.high_Score :
            
            self.high_Score = self.score
            
            with open("data.txt","w") as data:
                data.write(f"{self.high_Score}")
            
        self.score = 0
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
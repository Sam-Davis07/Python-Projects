from turtle import Screen
from paddle import Paddle
from ball_class import Ball
from time import sleep
from scoreboard import Scoreboard

Score = Scoreboard()

my_screen = Screen()

my_screen.title("Pong")
my_screen.setup(height=600 , width=800)
my_screen.bgcolor("black")
my_screen.tracer(0)

rpaddle = Paddle(350,0)
lpaddle = Paddle(-350,0)

ball = Ball()

my_screen.listen()
my_screen.onkey(lpaddle.goUp,"W")
my_screen.onkey(lpaddle.goDown,"S")
my_screen.onkey(rpaddle.goUp,"Up")
my_screen.onkey(rpaddle.goDown,"Down")


game_is_on = True

while game_is_on:
    sleep(ball.move_speed)
    my_screen.update()
    ball.move()    

    
    # Detect collision with wall
    if ((ball.ycor() > 280) or (ball.ycor() < -280)):
        ball.bounce_y()
    
    # Detect collision with padddle
    
    if ball.distance(rpaddle) < 50 and ball.xcor() > 320 or ball.distance(lpaddle) < 50 and  ball.xcor() < -320 :
        ball.bounce_x()

        # Detect R paddle misses
    
    if ball.xcor() > 380 :
        ball.reset_position()
        Score.l_point()
        
    # Detect L paddle misses
    
    if ball.xcor() < -380 :
        ball.reset_position()   
        Score.r_point() 
        
        
    
    
my_screen.exitonclick()

from turtle import Screen
from time import sleep
from food import Food
from snake import Snake
from scoreboard import Scoreboard


my_screen = Screen() 

my_screen.tracer(0)
my_screen.setup(width=600 , height=600)
my_screen.bgcolor('black')
my_screen.title("My snake Game")



snake = Snake()
food = Food()
scoreboard = Scoreboard()

my_screen.listen()
my_screen.onkey(snake.up,"Up")
my_screen.onkey(snake.down,"Down")
my_screen.onkey(snake.right,"Right")
my_screen.onkey(snake.left,"Left")


game_is_on = True

while game_is_on:

    my_screen.update()
    sleep(0.1)
    snake.move()
    
    # Detect collision with the food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() < -290 or snake.head.ycor() > 290 :
        
        scoreboard.reset()
        scoreboard.game_over()
        my_screen.update()
    
    for segment in snake.segments :
        
        if segment == snake.head :
        
            pass
        
        elif snake.head.distance(segment) < 10:
        
            scoreboard.reset()
            scoreboard.game_over()
            
            snake.reset()
            
            
            
        



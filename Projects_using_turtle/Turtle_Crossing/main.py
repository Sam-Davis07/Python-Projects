from turtle import Screen
import time
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

my_screen = Screen()
my_screen.bgcolor("white")
my_screen.title("Turtle Crossing Game")
my_screen.setup(width=600,height=600)
my_screen.tracer(0)

my_turtle = Player()

score = Scoreboard()

cars = CarManager()

my_screen.listen()

my_screen.onkey(my_turtle.move,"Up")

game_is_on = True

while game_is_on :
    time.sleep(0.1)
    my_screen.update()
    
    cars.create_car()
    cars.move_cars()
    
    for car in cars.all_cars:
        if  car.distance(my_turtle) < 35 :
            my_screen.update()
            game_is_on = False
            score.game_over()
            
        
    
    if my_turtle.is_at_finish_line():
        my_turtle.go_to_start()
        cars.level_up()
        score.increase_level()
    
my_screen.exitonclick()
    

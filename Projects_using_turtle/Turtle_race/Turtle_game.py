import turtle

import random

is_race_on = False

screen = turtle.Screen()
screen.setup(width=500,height=400)
user_bet = screen.textinput(title="Make your bet",prompt="Which turtle will win the race? Enter a color: ")
y_positions = [-70,-40,-10,20,50,80]
color = ["red","orange","yellow","green","blue","purple"]

all_turtle = []

for inedex_turtle in range(0,6):
    new_turtle = turtle.Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.goto(x=-230,y=y_positions[inedex_turtle])
    new_turtle.color(color[inedex_turtle])
    all_turtle.append(new_turtle)

if user_bet :
    is_race_on = True
    
while is_race_on:
    for t in all_turtle:
        if t.xcor() > 230 :
            winning_turtle = t.pencolor()
            is_race_on = False
            if winning_turtle == user_bet :
                print(f"You've won! The {winning_turtle} turtle is the winner")
            else:
                print(f"You've lost! The {winning_turtle} turtle is the winner")
        
        random_dist = random.randint(0,10)
        t.forward(random_dist)

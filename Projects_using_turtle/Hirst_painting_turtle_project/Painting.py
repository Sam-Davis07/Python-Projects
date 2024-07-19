# import colorgram

# colors = colorgram.extract('image.jpeg',80)

# rgb_colors = []

# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r,g,b)
#     rgb_colors.append(new_color)
# print(rgb_colors)


import turtle

import random

my_turtle = turtle.Turtle()
my_screen = turtle.Screen()

turtle.colormode(255)


color_list = [(224, 233, 227), (207, 160, 82), (54, 88, 130), (145, 91, 40), (140, 26, 49), (221, 207, 105), (132, 177, 203), (158, 46, 83), (45, 55, 104), (169, 160, 39), (129, 189, 143), (83, 20, 44), (37, 43, 67), (186, 94, 107), (187, 140, 170), (85, 120, 180), (59, 39, 31), (88, 157, 92), (78, 153, 165), (194, 79, 73), (45, 74, 78), (80, 74, 44), (161, 201, 218), (57, 125, 121), (219, 175, 187), (169, 206, 172), (219, 182, 169), (179, 188, 212), (48, 74, 73), (147, 37, 35), (43, 62, 61)]


my_turtle.penup()
my_turtle.setheading(225)
my_turtle.forward(300)
my_turtle.setheading(0)

number_of_dots = 100

for dot_count in range(1,number_of_dots+1):
    my_turtle.dot(20,random.choice(color_list))
    my_turtle.forward(50)
    
    if dot_count % 10 == 0 :
        my_turtle.setheading(90)
        my_turtle.forward(50)
        my_turtle.setheading(180)
        my_turtle.forward(500)
        my_turtle.setheading(0)

my_turtle.hideturtle()



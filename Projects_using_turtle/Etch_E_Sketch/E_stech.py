import turtle

my_turtle = turtle.Turtle()

my_screen = turtle.Screen()

my_turtle.speed("slowest")

def move_forward():
    my_turtle.forward(50)

def move_backward():
    my_turtle.backward(50)
    
def clockwise(): 
    my_turtle.right(my_turtle.heading() + 10)

def counter_clockwise():
    my_turtle.left(my_turtle.heading() - 10)

def clear():
    my_turtle.clear()
    my_turtle.penup()
    my_turtle.home()
    my_turtle.pendown()

turtle.listen()

turtle.onkey(move_forward,"W")

turtle.onkey(move_backward,"S")

turtle.onkey(counter_clockwise,"A")

turtle.onkey(clockwise,"D")

turtle.onkey(clear,"C")

my_screen.exitonclick()
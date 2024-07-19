import turtle

starting_positions = [(0,0),(-20,0),(-40,0)]
move_distance = 20

UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake():
    
    def __init__(self):
        self.segments = []
        self.Snake_Create()
        self.head = self.segments[0]
    
    def Snake_Create(self):
        
        for position in starting_positions:
            new_segment = turtle.Turtle()
            new_segment.shape("square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(position)
            self.segments.append(new_segment)
     
    def reset(self):
        for seg in self.segments:
            seg.goto(1000,1000)
            
        self.segments.clear()
        self.Snake_Create()
        self.head = self.segments[0]
        
    def add_segment(self,position):
        new_segment = turtle.Turtle()
        new_segment.shape("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)
                
    def extend(self):
        self.add_segment(self.segments[-1].position())
        
    def move(self):
        for seg_num in range(len(self.segments) - 1,0,-1):
            new_X = self.segments[seg_num - 1].xcor()
            new_Y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_X,new_Y)
        self.head.forward(move_distance)
        
    def up(self):
            if self.head.heading() != DOWN :
                self.head.setheading(UP)
        
    def down(self):
        if self.head.heading() != UP :
            self.head.setheading(DOWN)
    
    def right(self):
        if self.head.heading() != LEFT :    
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT :
            self.head.setheading(LEFT)
from turtle import Turtle
STARTING_POSITIIONS=[(20,0),(0,0),(-20,0)]
UP=90
DOWN=270
LEFT=180
RIGHT=0
class Snake:
    def __init__(self):
        self.segments=[]
        self.createSnake()
        self.head=self.segments[0]
    def createSnake(self):
        for position in STARTING_POSITIIONS:
            self.add_segment(position)
            
    def add_segment(self,position):
        turtle=Turtle('square')
        turtle.color("white")
        turtle.penup()
        turtle.goto(position)
        self.segments.append(turtle)
    def extend(self):
        self.add_segment(self.segments[-1].position());
    def move_snake(self):
         for i in range(len(self.segments)-1,0,-1):
            new_x=self.segments[i-1].xcor();
            new_y=self.segments[i-1].ycor();
            self.segments[i].goto(new_x,new_y)
         self.head.forward(20)
    
    def up(self):
        if(self.head.heading()!=DOWN):
            self.head.setheading(90)
    def down(self):
        if(self.head.heading()!=UP):
         self.head.setheading(270)
    def left(self):
        if(self.head.heading()!=RIGHT):
            self.head.setheading(180)
    def right(self):
        if(self.head.heading()!=LEFT):
            self.head.setheading(0)
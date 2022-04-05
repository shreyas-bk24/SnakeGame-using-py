#create a snake body
import turtle
from turtle import Turtle

#creating constants in global level

STARTING_POSITION=[(0,0),(-20,0),(-40,0)]
MOVE_DISTENCE=20
UP=90
DOWN=270
RIGHT=0
LEFT=180

class Snake:
#constructor

    def __init__(self):
        self.segments=[]
        self.create_snake()
        self.head=self.segments[0]

#method to create a snake

    def create_snake(self):
        for position in STARTING_POSITION:
            self.add_segment(position)

    def add_segment(self,position):
        new_seg=Turtle(shape="square")
        new_seg.color("white")
        new_seg.penup()
        new_seg.goto(position)
        self.segments.append(new_seg)

    def reset(self):
        for seg in self.segments:
            seg.goto(1000,1000)
        self.segments.clear()
        self.create_snake()
        self.head=self.segments[0]

    def extend(self):
        self.add_segment(self.segments[-1].position()) #to get the last segment and its position
#moving the snake by moving the last segment forward

    def move(self):
        for seg_num in range(len(self.segments) -1,0,-1):
            new_x=self.segments[seg_num -1].xcor()
            new_y=self.segments[seg_num -1].ycor()
            self.segments[seg_num].goto(new_x,new_y)
        self.head.forward(MOVE_DISTENCE)

#here we are using if condition to prevent the backward moment of snake
#functions to move the snake

    def up(self):
        if self.head.heading() !=DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() !=UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading()!=RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading()!=LEFT:
            self.head.setheading(RIGHT)














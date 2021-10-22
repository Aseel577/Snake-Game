from turtle import Turtle
MOVE_DISTANCE = 20
RIGHT = 0
UP = 90
LEFT = 180
DOWN = 270


class Snake():

    def __init__(self):
        self.segment = []

        self.snake_shape()

    def snake_shape(self):
        for position in range(3):
            self.add_segment(position)

    def add_segment(self, position):
        timy = Turtle("square")
        timy.penup()
        timy.color("white")
        timy.goto(x=0, y=0)
        timy.speed("fastest")

        self.segment.append(timy)


    def extend(self):
        self.add_segment(self.segment[-1].position())

    def reset(self):
        for seg in self.segment:
            seg.goto(x=1000, y=1000)
        self.segment.clear()
        self.snake_shape()
        self.segment[0]




    def move(self):
        for seg in range(len(self.segment) - 1, 0, -1):
            xcor = self.segment[seg - 1].xcor()
            ycor = self.segment[seg - 1].ycor()
            self.segment[seg].goto(x=xcor, y=ycor)
        self.segment[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.segment[0].heading() != DOWN:
            self.segment[0].setheading(UP)

    def left(self):
        if self.segment[0].heading() != RIGHT:
            self.segment[0].setheading(LEFT)

    def right(self):
        if self.segment[0].heading() != LEFT:
            self.segment[0].setheading(RIGHT)

    def down(self):
        if self.segment[0].heading() != UP:
            self.segment[0].setheading(DOWN)






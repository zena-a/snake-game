from turtle import Turtle

# Constants are great for concrete values in case you need to change it
STARTING_POS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    # Constructor - These attributes and methods are called once
    # an object is declared
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    # The snake body is created by making a list containing segments
    def create_snake(self):
        for position in STARTING_POS:
            self.add_segment(position)

    # Adds a new segment to the snake's body from the tail end
    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    # Once the snake scores a point, this extends the body
    def extend(self):
        self.add_segment(self.segments[-1].position())

    # The snake moves forward, with the last segment replacing
    # the one before it
    # Range is used here to count backwards in a list
    # range(start, stop, step)
    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)

        self.head.forward(MOVE_DISTANCE)

    # Changes snake's orientation either up, down, left or right
    # Prevents snake from going backwards
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

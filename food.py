from turtle import Turtle
import random

COLORS = ["red", "blue", "yellow", "green", "purple", "orange"]


class Food(Turtle):

    # Constructor that sets values food object when initialized
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.shapesize(stretch_len=1, stretch_wid=1)
        self.color(random.choice(COLORS))
        self.refresh()

    # Changes food location on screen
    def refresh(self):
        self.speed("fastest")
        self.color(random.choice(COLORS))
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)

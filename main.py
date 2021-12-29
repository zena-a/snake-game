# Snake Game - Using Turtle Package, Understanding Documentation and Using OOP Concepts
from turtle import Screen, Turtle
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

# Sets screen
screen = Screen()
screen.setup(width=650, height=650)
screen.bgcolor("black")
screen.title("Feed Your Pet Snake")
# Turns the animation off until update() function is called
screen.tracer(0)

# Draw border
border_pen = Turtle()
border_pen.color("red")
border_pen.hideturtle()
border_pen.penup()
border_pen.goto(-300, 300)
for _ in range(4):
    border_pen.pendown()
    border_pen.forward(600)
    border_pen.right(90)

# Creating our objects for the different classes
snake = Snake()
food = Food()
scoreboard = Scoreboard()

# Event listeners and key binders
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True

while game_is_on:
    # Updates the screen to show the snake body
    screen.update()
    # Suspends execution of the loop for 0.1 seconds
    # Makes it look like the body is moving together
    time.sleep(0.1)

    snake.move()

    # Detect collision with food use turtle.distance()
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()

    # Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()

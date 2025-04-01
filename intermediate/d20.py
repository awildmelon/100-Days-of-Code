
# Day 20 & 21 - Snake Game - 23/03/2025

from turtle import Screen
from packages.d20.snake import Snake
from packages.d20.food import Food
from packages.d20.score import Score
import time

# Screen setup

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("snek game")
screen.tracer(0)

# Snake, food, and score setup

snek = Snake()
yums = Food()
score = Score()

# Detects key presses

screen.listen()
screen.onkey(snek.up, "Up")
screen.onkey(snek.down, "Down")
screen.onkey(snek.left, "Left")
screen.onkey(snek.right, "Right")

# Restart game function

def restart_game():
    global game_on
    game_on = True
    snek.__init__()
    yums.refresh()
    score.reset()

# Snake movement

game_on = True

while game_on:
    screen.update()
    time.sleep(0.1)
    snek.move()

    # Detect collision with food
    
    if snek.head.distance(yums) < 15:
        yums.refresh()
        snek.grow()
        score.increase_score()

    # Detect collision with wall

    if (
        snek.head.xcor() > 290 or snek.head.xcor() < -290 or
        snek.head.ycor() > 290 or snek.head.ycor() < -290
    ):
        game_on = False
        score.game_over()

    # Detect collision with tail

    for segment in snek.segments[1:]:
        if snek.head.distance(segment) < 10:
            game_on = False
            score.game_over()

screen.exitonclick()
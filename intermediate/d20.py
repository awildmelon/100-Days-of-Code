# Day 20 - Snake Game - 23/03/2025

from turtle import Screen
from packages.d20.snake import Snake
import time

# Screen setup

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("snek game")
screen.tracer(0)

# Snake setup

snek = Snake()

# Detects key presses

screen.listen()
screen.onkey(snek.up, "Up")
screen.onkey(snek.down, "Down")
screen.onkey(snek.left, "Left")
screen.onkey(snek.right, "Right")

# Snake movement

game_on = True

while game_on:
    screen.update()
    time.sleep(0.1)
    
    snek.move()

screen.exitonclick()

# Day 22 - Pong Game - 31/03/2025

from turtle import Screen, Turtle
from packages.d22.paddle import Paddle
from packages.d22.ball import Ball
from packages.d22.score import Score
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

# Paddle, ball, and score setup

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

ball = Ball()
score = Score()

game_on = True

while game_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

    # Detect wall collision and bounce

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.y_bounce()
    
    # Detect paddle collision

    if (ball.xcor() > 320 and ball.xcor() < 340) and (ball.distance(r_paddle) < 50):
        ball.x_bounce()

    if (ball.xcor() < -320 and ball.xcor() > -340) and (ball.distance(l_paddle) < 50):
        ball.x_bounce()

    # Detect ball out of bounds

    if ball.xcor() > 380:
        ball.reset_position()
        l_paddle.reset_position()
        r_paddle.reset_position()
        score.l_point()
        ball.x_bounce()

    if ball.xcor() < -380:
        ball.reset_position()
        l_paddle.reset_position()
        r_paddle.reset_position()
        score.r_point()
        ball.x_bounce()

screen.exitonclick()
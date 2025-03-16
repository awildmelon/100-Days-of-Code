from turtle import Turtle, Screen
import random

timmy = Turtle()
print(timmy)

screen = Screen()
screen.title("Turtle Graphics")
screen.bgcolor("white")

timmy.shape("turtle")
timmy.speed("fastest")

for i in range(72):
    timmy.color(random.random(), random.random(), random.random())
    timmy.circle(100)
    timmy.left(5)

print(screen.canvheight)

screen.exitonclick()
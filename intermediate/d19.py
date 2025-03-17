# Day 19 - Turtle Race - 16/03/2025

import turtle as Turtle
import random

# Screen setup

screen = Turtle.Screen()
screen.title("Turtle Race")
screen.setup(width=800, height=400)

# Turtle setup

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtles = []

for i in range(6):
    t = Turtle.Turtle()
    t.shape("turtle")
    t.color(colors[i])
    t.penup()
    t.goto(-300, 125 - i * 50)
    turtles.append(t)

# Draw finish line
finish_line = Turtle.Turtle()
finish_line.penup()
finish_line.goto(300, 150)
finish_line.pendown()
finish_line.right(90)
finish_line.forward(300)
finish_line.hideturtle()

# Player bets on a turtle

player_bet = screen.textinput(title="Bet on a turtle.", prompt="Which turtle will win the race?")
player_bet = player_bet.lower()

if player_bet not in colors:
    print("Invalid")

# Race starts and program checks which turtle wins

if player_bet:
    race_on = True

while race_on:
    for turtle in turtles:
        if turtle.xcor() > 300:
            race_on = False
            if turtle.pencolor() == player_bet:
                print(f"You win! The {turtle.pencolor()} turtle won!")
            else:
                print(f"You lose. The {turtle.pencolor()} turtle won...")

        distance = random.randint(0, 10)
        turtle.forward(distance)

screen.exitonclick()
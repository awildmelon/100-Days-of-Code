
# Day 23 - Turtle Crossing - 01/04/2025

import time
from turtle import Screen
from packages.d23.player import Player
from packages.d23.car_manager import CarManager
from packages.d23.scoreboard import Scoreboard

# Screen setup

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.title("Turtle Crossing")

# Plyaer, car and scoreboard setup

player = Player()
cars = CarManager()
scoreboard = Scoreboard()

# Movement keys

screen.listen()
screen.onkey(player.move, "Up")
screen.onkey(player.move, "w")

# Game loop

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    cars.move_cars()

    # Finish line and next level

    if player.at_finish_line():
        player.reset_position()
        scoreboard.level_up()
        cars.reset_cars()
        cars.increase_speed()

    # Collision detection with cars and game over

    for car in cars.all_cars:
        if player.player.distance(car) < 20:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
CARS = 10
SPEED_MULTIPLIER = 1.5

from turtle import Turtle
import random

class CarManager:
    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE
        self.create_cars()
        self.move_cars()

    # Create cars at random positions with random colors
    def create_cars(self):
        for _ in range(CARS):
            new_car = Turtle("square")
            new_car.color(COLORS[_ % len(COLORS)])
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            random_x = random.randint(-300, 300)
            random_y = random.randint(-240, 240)
            new_car.goto(random_x, random_y)
            self.all_cars.append(new_car)

    # Move cars to the left and reset their position if they go off-screen
    def move_cars(self):
        for car in self.all_cars:
            car.setx(car.xcor() - self.car_speed)
            if car.xcor() < -320:
                car.goto(300, random.randint(-240, 240))
                car.setx(car.xcor() - self.car_speed)

    # Reset all cars to random positions after each level
    def reset_cars(self):
        for car in self.all_cars:
            random_x = random.randint(-300, 300)
            random_y = random.randint(-240, 240)
            car.goto(random_x, random_y)

    # Increase car speed after each level by a multiplier
    def increase_speed(self):
        self.car_speed *= SPEED_MULTIPLIER
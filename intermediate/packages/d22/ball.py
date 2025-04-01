from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.goto(0, 0)
        self.x_move = 10
        self.y_move = 10

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def increase_speed(self):
        self.x_move *= 1.1
        self.y_move *= 1.1

    def y_bounce(self):
        self.y_move *= -1

    def x_bounce(self):
        self.x_move *= -1
        self.increase_speed()

    def reset_position(self):
        self.goto(0, 0)
        self.x_bounce()
        self.y_bounce()
        self.x_move = 10
        self.y_move = 10
from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)

    def go_up(self):
        new_y = self.ycor()
        if new_y < 250:
            self.sety(new_y + 20)

    def go_down(self):
        new_y = self.ycor()
        if new_y > -240:
            self.sety(new_y - 20)

    def reset_position(self):
        self.goto(self.xcor(), 0)
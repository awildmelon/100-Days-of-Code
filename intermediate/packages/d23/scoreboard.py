FONT = ("Courier", 24, "normal")

from turtle import Turtle

class Scoreboard:
    def __init__(self):
        self.level = 1
        self.pen = Turtle()
        self.pen.color("black")
        self.pen.penup()
        self.pen.hideturtle()
        self.pen.goto(0, 260)
        self.update_scoreboard()

    # Display the current level on the screen
    def update_scoreboard(self):
        self.pen.clear()
        self.pen.write(f"Level: {self.level}", align="center", font=FONT)
        self.pen.goto(0, 260)

    # Increase level when player reaches the finish line
    def level_up(self):
        self.level += 1
        self.update_scoreboard()

    # Game over message when player collides with a car, display final level
    def game_over(self):
        self.pen.goto(0, 0)
        self.pen.color("red")
        self.pen.write("GAME OVER", align="center", font=FONT)
        self.pen.goto(0, -30)
        self.pen.color("black")
        self.pen.write(f"Final Level: {self.level}", align="center", font=FONT)

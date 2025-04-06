from turtle import Turtle
import os

class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score_file = os.path.join(os.path.dirname(__file__), "high_score.txt")
        self.high_score = self.read_high_score()
        self.color("white")
        self.penup()
        self.goto(0, 260)
        self.hideturtle()
        self.update_scoreboard()

    def read_high_score(self):
        try:
            with open(self.high_score_file, "r") as file:
                return int(file.read())
        except (FileNotFoundError, ValueError):
            return 0

    def save_high_score(self):
        with open(self.high_score_file, "w") as file:
            file.write(str(self.high_score))

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align="center", font=("Comic Sans MS", 24, "normal"))

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.save_high_score()
        self.score = 0
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 15
FINISH_LINE_Y = 280

from turtle import Turtle

class Player:
    def __init__(self):
        self.player = Turtle()
        self.player.shape("turtle")
        self.player.penup()
        self.player.goto(STARTING_POSITION)
        self.player.setheading(90)

    # Move player up
    def move(self):
        self.player.forward(MOVE_DISTANCE)

    # Reset player position after every level
    def reset_position(self):
        self.player.goto(STARTING_POSITION)

    # Check if the player has reached the finish line
    def at_finish_line(self):
        if self.player.ycor() > FINISH_LINE_Y:
            return True
        return False

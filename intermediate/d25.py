
# Day 25 - U.S. States Game - 12/04/2025

import pandas as pd
import turtle as t

# Screen setup

screen = t.Screen()
screen.title("U.S. States Game")
screen.setup(width=725, height=491)
screen.bgcolor("lightblue")
screen.tracer(0)

# Set GIF file from packages as background

screen.bgpic("c:/Users/kevin/OneDrive/Documents/coding/python/100 Days of Python/100-Days-of-Code/intermediate/packages/d25/blank_states_img.gif")

# Data loading

data = pd.read_csv("c:/Users/kevin/OneDrive/Documents/coding/python/100 Days of Python/100-Days-of-Code/intermediate/packages/d25/50_states.csv")
states = data["state"].to_list()
x = data["x"].to_list()
y = data["y"].to_list()
state_coords = {state: (x[i], y[i]) for i, state in enumerate(states)}

# Guessing game

guessed_states = []
correct_guesses = 0
incorrect_guesses = 0

while correct_guesses < 50:
    answer = screen.textinput(title=f"{correct_guesses}/50 States Correct", prompt="Name a state!")
    
    if answer is None:  # If the user clicks cancel
        break

    answer = answer.title()

    if answer in states and answer not in guessed_states:
        guessed_states.append(answer)
        correct_guesses += 1

        # Turtle for every correct state guessed

        t.penup()
        t.hideturtle()
        t.goto(state_coords[answer])
        t.write(answer, align="center", font=("Arial", 8, "normal"))

    elif answer == "Exit":
        break

    else:
        incorrect_guesses += 1

# Game over screen

if correct_guesses < 50:
    missed_states = [state for state in states if state not in guessed_states]
    game_result = "You Lose... :("
    
    # Missed states saved as a CSV file

    missed_states_df = pd.DataFrame(missed_states, columns=["Missed States"])
    missed_states_df.to_csv(
        "c:/Users/kevin/OneDrive/Documents/coding/python/100 Days of Python/100-Days-of-Code/intermediate/packages/d25/missed_states.csv",
        index=False
    )
else:
    game_result = "You Win! :)"

t.penup()
t.hideturtle()

t.goto(-150, 100)
t.fillcolor("white")
t.begin_fill()
for _ in range(2):
    t.forward(300)
    t.right(90)
    t.forward(100)
    t.right(90)
t.end_fill()

# Display stats

t.goto(0, 0)
t.write(
    f"{game_result}\nCorrect Guesses: {correct_guesses}/50\nIncorrect Guesses: {incorrect_guesses}\nMissed States: {len(missed_states) if correct_guesses < 50 else 0}",
    align="center",
    font=("Arial", 16, "bold")
)

screen.mainloop()
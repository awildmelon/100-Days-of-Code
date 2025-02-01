
# Day 12 - Guess the Number - 18/01/2025

import random

print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")

difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

mystery_number = random.randint(1, 100)
answer = 0

if difficulty == "easy":
    attempts = 10
else:
    attempts = 5

while attempts != 0:
    print(f"You have {attempts} attempts remaining to guess the mystery number.")
    answer = int(input("Make a guess: "))

    if answer > mystery_number:
        print("Too high.")
    elif answer < mystery_number:
        print("Too low.")
    else:
        break

    attempts -= 1

if answer != mystery_number:
    print(f"You've run out of guesses. The mystery number was {mystery_number}.")
else:
    print(f"You got it! The mystery number was {mystery_number}.")
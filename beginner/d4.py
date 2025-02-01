
# Day 4 - Rock, Paper, Scissors - 10/01/2025

import random

print("Welcome to Rock, Paper, Scissors!")
print("Please choose one of the following:")
print("1. Rock\n2. Paper\n3. Scissors")

player_choice = input("Enter your choice: ")

choice = {
    "1": "Rock",
    "2": "Paper",
    "3": "Scissors"
}

if player_choice in choice:
    print(f"You chose {choice[player_choice]}")
else:
    print("Invalid choice. Please try again.")

computer_choice = random.choice(["1", "2", "3"])
print(f"The computer chose {choice[computer_choice]}")

result = {
    (player_choice == computer_choice): "It's a tie!",
    (player_choice == "1" and computer_choice == "3"): "You win!",
    (player_choice == "2" and computer_choice == "1"): "You win!",
    (player_choice == "3" and computer_choice == "2"): "You win!"
}

print(result.get(True, "You lose!"))

# Day 14 - Higher Lower Game - 20/01/2025

import random

game = True
countries = ["India", "China", "United States", "Indonesia", "Pakistan", "Nigeria", "Brazil", "Bangladesh", "Russia","Ethiopia", "Mexico"]
score = 0

print("Welcome to the Higher Lower Game.")
print("You will have to guess if the country A or country B have a greater population.")


countryA = random.choice(countries)

while game == True:
    countryB = random.choice(countries)

    while countryA == countryB:
        countryB = random.choice(countries)

    print(f"Country A: {countryA}")
    print("VS")
    print(f"Country B: {countryB}")

    answer = input("A or B? ").lower()

    if answer == "b":
        if countries.index(countryA) > countries.index(countryB):
            print("You guessed right!")
            score += 1
        else:
            print(f"You guessed wrong!\nNice try. Score: {score}")
            game = False
    else:
        if countries.index(countryA) < countries.index(countryB):
            print("You guessed right!")
            score += 1
        else:
            print(f"You guessed wrong!\nNice try. Score: {score}")
            game = False

    if score == 10:
        print("Congratulations! You've won the game with a score of 10.")
        game = False

    countryA = countryB
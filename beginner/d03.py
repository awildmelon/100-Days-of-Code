
# Day 3 - Treasure Island - 09/01/2025

print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

choice1 = input('You\'re at a crossroad, where do you want to go? Type "left" or "right"\n').lower()

if choice1 == "left":
    choice2 = input('You\'ve come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across.\n').lower()
    if choice2 == "wait":
        choice3 = input('You arrive at the island but the boat exploded. There is a house with 3 doors. One red, one yellow and one blue. Which color do you choose?\n').lower()
        if choice3 == "red":
            print("It's a room full of goblins. They kidnapped you and took you to their cave. Game Over.")
        elif choice3 == "yellow":
            print("You found the treasure! It was filled with coins and jewels! You Win!")
        elif choice3 == "blue":
            print("You enter an empty room. The door behind you shut and poison gas filled the room. Game Over.")
        else:
            print("You looked for a door that didn't exist for the rest of eternity. Game Over.")
    else:
        print("You drowned because you forgot how to swim. Game Over.")
else:
    print("You tripped on a rock and cracked your skull. Game Over.")

# Day 11 - Blackjack - 17/01/2025

import random

def deal_card():
    """Returns a random card from the deck."""
    cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
    return random.choice(cards)

def calculate_score(cards):
    """Take a list of cards and return the score calculated from the cards."""
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(user_score, computer_score):
    """Compare the user and computer scores and return the result."""
    if user_score == computer_score:
        return "Draw! 🙃"
    elif computer_score == 0 or computer_score == 21:
        return "Lose, opponent has Blackjack! 😱"
    elif user_score == 0 or user_score == 21:
        return "Win with a Blackjack! 😎"
    elif user_score > 21:
        return "You went over. You lose! 😭"
    elif computer_score > 21:
        return "Opponent went over. You win! 😁"
    elif user_score > computer_score:
        return "You win! 😃"
    else:
        return "You lose! 😤"

def play_game():
    print("Welcome to Blackjack!")

    user_cards = [deal_card() for _ in range(2)]
    computer_cards = [deal_card() for _ in range(2)]
    is_game_over = False

    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")

        if user_score == 0 or user_score == 21 or computer_score == 0 or computer_score == 21 or user_score > 21:
            is_game_over = True
        else:
            should_continue = input("Type 'y' to get another card, type 'n' to pass: ")
            if should_continue == "y":
                new_card = deal_card()
                if new_card == 11:
                    ace_value = input("You got an Ace! Do you want it to be 1 or 11? ")
                    new_card = 1 if ace_value == "1" else 11
                user_cards.append(new_card)
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    play_game()

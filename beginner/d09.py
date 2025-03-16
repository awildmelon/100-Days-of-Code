
# Day 9 - Silent Auction - 15/01/2025

names = []

def add_bidder(name, bid):
    names.append({"name": name, "bid": bid})

def find_winner():
    highest_bid = 0
    winner = ""
    for name in names:
        if name["bid"] > highest_bid:
            highest_bid = name["bid"]
            winner = name["name"]
    return winner

print("Welcome to the Silent Auction.")

while True:
    name = input("What is your name?\n")
    bid = int(input("What is your bid?\n"))
    add_bidder(name, bid)

    more_bidders = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
    if more_bidders == "no":
        break

print(f"The winner is {find_winner()} with a bid of ${max([name['bid'] for name in names])}.")
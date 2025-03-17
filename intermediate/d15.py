
# Day 15 - Coffee Machine - 21/01/2025

coffee_type = input("What would you like? (espresso/latte/cappuccino): ").lower()

menu = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18
        },
        "cost": 1.50
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24
        },
        "cost": 2.50
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24
        },
        "cost": 3.00
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0
}

def is_resource_sufficient(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True

def process_coins():
    print("Please insert coins.")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickels = int(input("How many nickels?: "))
    pennies = int(input("How many pennies?: "))
    return quarters * 0.25 + dimes * 0.10 + nickels * 0.05 + pennies * 0.01

def make_coffee(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name}. Enjoy!")

if coffee_type == "report":
    print(f"Water: {resources['water']}ml\nMilk: {resources['milk']}ml\nCoffee: {resources['coffee']}g\nMoney: ${resources['money']}")
elif coffee_type == "off":
    pass
else:
    drink = menu[coffee_type]
    if is_resource_sufficient(drink["ingredients"]):
        payment = process_coins()
        if payment >= drink["cost"]:
            change = round(payment - drink["cost"], 2)
            print(f"Here is ${change} in change.")
            resources["money"] += drink["cost"]
            make_coffee(coffee_type, drink["ingredients"])
        else:
            print("Sorry, that's not enough money. Money refunded.")
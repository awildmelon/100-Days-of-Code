
# Day 5 - PyPassword Generator - 11/01/2025

import random

print("Welcome to PyPassword Generator!")
letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "!@#$%^&*()_+"

num_letters = int(input("How many letters would you like in your password? "))
num_numbers = int(input("How many numbers would you like in your password? "))
num_symbols = int(input("How many symbols would you like in your password? "))

password = ""

for _ in range(num_letters):
    password += random.choice(letters)

for _ in range(num_numbers):
    password += random.choice(numbers)

for _ in range(num_symbols):
    password += random.choice(symbols)

password = ''.join(random.sample(password, len(password)))

print(f"Your password is: {password}")
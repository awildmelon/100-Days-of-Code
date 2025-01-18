
# Day 8 - Caesar Cipher - 14/01/2025

import string

def caesar(text, shift, direction):
    if direction == "decode":
        shift *= -1
    return "".join([chr((ord(char) - 97 + shift) % 26 + 97) if char.isalpha() else char for char in text])

print("Welcome to the Caesar Cipher.")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")

print(f"Here's the {direction}d result: {caesar(text, shift, direction)}")
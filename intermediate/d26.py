
# Day 26 - NATO Phonetic Alphabet - 25/04/2025

import pandas as pd
import os

base_path = os.path.dirname(__file__)
data = pd.read_csv(os.path.join(base_path, "packages", "d26", "nato_phonetic_alphabet.csv"))


phonetic_dict = {row.letter: row.code for _, row in data.iterrows()}

def generate_phonetic(word):
    try:
        letters_list = [phonetic_dict[letter] for letter in word]
    except KeyError as e:
        print("Sorry, only letters in the alphabet are allowed. Please try again.")
        generate_phonetic(input("Enter a word: ").upper())
    else:
        print(letters_list)

word = input("Enter a word: ").upper()
generate_phonetic(word)
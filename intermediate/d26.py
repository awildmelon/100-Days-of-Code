
# Day 26 - NATO Phonetic Alphabet - 25/04/2025

import pandas as pd
import os

base_path = os.path.dirname(__file__)
data = pd.read_csv(os.path.join(base_path, "packages", "d26", "nato_phonetic_alphabet.csv"))

# Dictionary made using NATO Phonetic Alphabet CSV file
# dictionary_comprehension = {new_key: new_value for item in list}
# new_dict = {new_key: new_value for (key, value) in dict.items() if condition}

phonetic_dict = {row.letter: row.code for _, row in data.iterrows()}

# User inputs a word, which is converted into a list of letters
# list_comprehension = [new_item for item in list if condition]

word = input("Enter a word: ").upper()
letters_list = [letter for letter in word]

# Each letter is replaced with the corresponding phonetic code

phonetic_list = [phonetic_dict[letter] for letter in letters_list if letter in phonetic_dict]

print(phonetic_list)

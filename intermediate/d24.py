
# Day 24 - Mail Merge - 06/04/2025

import os

# Setup for file paths

base_path = os.path.dirname(__file__)
names_path = os.path.join(base_path, "packages", "d24", "Input", "Names", "invited_names.txt")
template_path = os.path.join(base_path, "packages", "d24", "Input", "Letters", "starting_letter.txt")

# Reads names from the file

with open(names_path, "r") as f:
    names = f.readlines()

names = [name.strip() for name in names]

# Reads template letter

with open(template_path, "r") as f:
    template = f.read()

# Creates personalized letters for each name by replacing placeholder and saves them

for name in names:
    personalized_letter = template.replace("[name]", name)
    output_path = os.path.join(base_path, "packages", "d24", "Output", f"letter_to_{name}.txt")
    with open(output_path, "w") as f:
        f.write(personalized_letter)
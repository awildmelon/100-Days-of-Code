# Day 30 - Flash Card App - 18/08/2026

from tkinter import *
import os
import random
import pandas as pd

BACKGROUND_COLOR = "#B1DDC6"
language = "Indonesian"
current_word = None

# -------------------------- RANDOM WORD SELECTION ------------------------------- #

base_path = os.path.dirname(__file__)
original_data_path = os.path.join(base_path, "packages", "d30", "indonesian_words.csv")
learned_data_path = os.path.join(base_path, "packages", "d30", "words_to_learn.csv")

# If learned file doesn't exist, make a copy of the original file
if not os.path.exists(learned_data_path):
	learned_data = pd.read_csv(original_data_path)
	learned_data.to_csv(learned_data_path, index=False)

data = pd.read_csv(learned_data_path)
to_study = data.to_dict(orient="records")

current_word = random.choice(to_study)

def next_word():
    global current_word
    current_word = random.choice(to_study)
    canvas.itemconfig(card_image, image=card_front_image)
    canvas.itemconfig(given_word_label, text=current_word["Indonesian"], fill="black")
    canvas.itemconfig(language_label, text=language, fill="black")

    right_button.config(state=NORMAL)
    wrong_button.config(state=NORMAL)

# -------------------------- BUTTON SETUP ------------------------------- #

def show_indonesian():
	global language
	language = "Indonesian"
	canvas.itemconfig(card_image, image=card_front_image)
	canvas.itemconfig(given_word_label, text=current_word[language], fill="black")
	canvas.itemconfig(language_label, text=language, fill="black")

def show_english():
	global language
	language = "English"
	canvas.itemconfig(card_image, image=card_back_image)
	canvas.itemconfig(given_word_label, text=current_word[language], fill="white")
	canvas.itemconfig(language_label, text=language, fill="white")
	window.after(3000, show_indonesian)

def mark_as_known():
	global current_word, data
	# Prevents buttons from being spammed when the card is flipping
	right_button.config(state=DISABLED)
	wrong_button.config(state=DISABLED)
	
	data = data[data["Indonesian"] != current_word["Indonesian"]]
	data.to_csv(learned_data_path, index=False)
	to_study.remove(current_word)
	
	# If all the words are learned, reset to original file
	if len(to_study) == 0:
		data = pd.read_csv(original_data_path)
		data.to_csv(learned_data_path, index=False)
		to_study.clear()
		to_study.extend(data.to_dict(orient="records"))
	
	next_word()

def mark_as_unknown():
	global current_word
	# Prevents buttons from being spammed when the card is flipping
	right_button.config(state=DISABLED)
	wrong_button.config(state=DISABLED)

	show_english()
	window.after(3000, next_word)

# -------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Flash Card App")
window.config(
    padx=50,
    pady=50,
    bg=BACKGROUND_COLOR
)

card_front_path = os.path.join(base_path, "packages", "d30", "card_front.png")
card_back_path = os.path.join(base_path, "packages", "d30", "card_back.png")
right_image_path = os.path.join(base_path, "packages", "d30", "right.png")
wrong_image_path = os.path.join(base_path, "packages", "d30", "wrong.png")

card_front_image = PhotoImage(file=card_front_path)
card_back_image = PhotoImage(file=card_back_path)
right_image = PhotoImage(file=right_image_path)
wrong_image = PhotoImage(file=wrong_image_path)

# Canvas Setup

canvas = Canvas(
	width=800,
	height=526,
	bg=BACKGROUND_COLOR,
	highlightthickness=0,
)
card_image = canvas.create_image(400, 263, image=card_front_image)

canvas.grid(row=0, column=0, columnspan=2)

# Buttons Setup

right_button = Button(
    image=right_image,
    highlightthickness=0,
    command=mark_as_known
)
wrong_button = Button(
	image=wrong_image,
    highlightthickness=0,
    command=mark_as_unknown
)

right_button.grid(row=1, column=1)
wrong_button.grid(row=1, column=0)

# Text Setup

language_label = canvas.create_text(
	400,
	150,
	text=language,
	font=("Arial", 30, "italic"),
	fill="black"
)

given_word_label = canvas.create_text(
	400,
	263,
	text=current_word["Indonesian"],
	font=("Arial", 40, "bold"),
	fill="black"
)

window.mainloop()


# Day 28 - Pomadoro Timer - 12/08/2026

from tkinter import *
import os

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Comic Sans MS"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro Timer")
window.config(padx=100, pady=50, bg=YELLOW)

base_path = os.path.dirname(__file__)
image_path = os.path.join(base_path, "packages", "d28", "tomato.png")
tomato_image = PhotoImage(file=image_path)


canvas = Canvas(width=200, height=280, bg=YELLOW, highlightthickness=0)
canvas.create_image(100, 160, image=tomato_image)
canvas.create_text(100, 175, text="00:00", font=(FONT_NAME, 35, "bold"), fill = "white")
canvas.create_text(100, 15, text="Timer", font=(FONT_NAME, 25, "bold"), fill = GREEN)

canvas.grid(row=0, column=1)


start_button = Button(window, text="Start", highlightthickness=0, command=None)
reset_button = Button(window, text="Reset", highlightthickness=0, command=None)

start_button.grid(row=1, column=0)
reset_button.grid(row=1, column=2)


window.mainloop()
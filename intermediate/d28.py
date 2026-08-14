
# Day 28 - Pomadoro Timer - 12/08/2026

from tkinter import *
import os

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Comic Sans MS"
WORK_MIN = 1
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global reps
    reps += 1

    if reps % 8 == 0:
        count_down(LONG_BREAK_MIN * 60)
        canvas.itemconfig(title_label, text="Break", fill=RED)
    elif reps % 2 == 0:
        count_down(SHORT_BREAK_MIN * 60)
        canvas.itemconfig(title_label, text="Break", fill=PINK)
    else:
        count_down(WORK_MIN * 60)
        canvas.itemconfig(title_label, text="Work", fill=GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(count):
    canvas.itemconfig(timer_text, text=f"{count // 60:02d}:{count % 60:02d}")
    if count > 0:
        window.after(1000, count_down, count - 1)
    else:
        start_timer()

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro Timer")
window.config(padx=100, pady=50, bg=YELLOW)

base_path = os.path.dirname(__file__)
image_path = os.path.join(base_path, "packages", "d28", "tomato.png")
tomato_image = PhotoImage(file=image_path)


canvas = Canvas(width=200, height=280, bg=YELLOW, highlightthickness=0)
canvas.create_image(100, 160, image=tomato_image)
timer_text = canvas.create_text(100, 175, text="00:00", font=(FONT_NAME, 35, "bold"), fill = "white")
title_label = canvas.create_text(100, 15, text="Timer", font=(FONT_NAME, 25, "bold"), fill = GREEN)

canvas.grid(row=0, column=1)



start_button = Button(window, text="Start", highlightthickness=0, command=start_timer)
reset_button = Button(window, text="Reset", highlightthickness=0, command=None)

start_button.grid(row=1, column=0)
reset_button.grid(row=1, column=2)


window.mainloop()
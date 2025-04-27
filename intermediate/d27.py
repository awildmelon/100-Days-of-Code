# Day 27 - Mile to Kilometer Converter - 26/04/2025

from tkinter import Tk, Label, Entry, Button

# Screen setup

screen = Tk()
screen.title("Mile to Km Converter")
screen.minsize(width=300, height=150)
screen.config(padx=20, pady=20)

# Miles entry and label

mil_entry = Entry(width=10)
mil_entry.grid(column=1, row=0)

mil_label = Label(text="Miles", font=("Arial", 12))
mil_label.grid(column=2, row=0)

# "is equal to" label

equal_label = Label(text="is equal to", font=("Arial", 12))
equal_label.grid(column=0, row=1)

# Kilometers result and label

km_result_label = Label(text="0", font=("Arial", 12))
km_result_label.grid(column=1, row=1)

km_label = Label(text="Km", font=("Arial", 12))
km_label.grid(column=2, row=1)

# Conversion function

def convert_miles_to_km():
    try:
        miles = float(mil_entry.get())
        kilometers = round(miles * 1.60934, 2)
        km_result_label.config(text=str(kilometers))
    except ValueError:
        km_result_label.config(text="Invalid")

# Conversion button

convert_button = Button(text="Calculate", command=convert_miles_to_km, font=("Arial", 12))
convert_button.grid(column=1, row=2)

screen.mainloop()
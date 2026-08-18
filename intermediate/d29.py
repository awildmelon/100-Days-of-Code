
# Day 29 - Password Manager - 14/08/2026

from tkinter import *
from tkinter import messagebox
import os
import random
import json

try:
    import pyperclip
except ImportError:
    pyperclip = None

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numbers = "0123456789"
    symbols = "!@#$%^&*()_+"

    num_letters = random.randint(8, 10)
    num_numbers = random.randint(2, 4)
    num_symbols = random.randint(2, 4)

    password_list = []

    for _ in range(num_letters):
        password_list.append(random.choice(letters))

    for _ in range(num_numbers):
        password_list.append(random.choice(numbers))

    for _ in range(num_symbols):
        password_list.append(random.choice(symbols))

    random.shuffle(password_list)

    password = ''.join(password_list)

    password_entry.delete(0, END)
    password_entry.insert(0, password)

    if pyperclip is not None:
        pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_credentials():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    is_ok = messagebox.askokcancel(
        title="Confirmation",
        message=f"These are the details entered:\n \nWebsite: {website}\nEmail: {email}\nPassword: {password}\n\nDo you want to save these credentials?"
    )

    if website and email and password and is_ok:
        file_path = os.path.join(base_path, "packages", "d29", "password_data.json")

        if os.path.exists(file_path):
            with open(file_path, "r") as file:
                try:
                    data = json.load(file)
                except json.JSONDecodeError:
                    data = []
        else:
            data = []

        data.append({
            "website": website,
            "email": email,
            "password": password
        })

        with open(file_path, "w") as file:
            json.dump(data, file, indent=4)

        website_entry.delete(0, END)
        email_entry.delete(0, END)
        email_entry.insert(0, "example@gmail.com")
        password_entry.delete(0, END)

        messagebox.showinfo(title="Success", message="Login credentials saved successfully!")

    elif not is_ok:
        return
    else:
        messagebox.showwarning(title="Warning", message="Please fill in all fields before saving.")

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

base_path = os.path.dirname(__file__)
image_path = os.path.join(base_path, "packages", "d29", "logo.png")
logo_image = PhotoImage(file=image_path)


canvas = Canvas(width=200, height=200)
canvas.create_image(100, 100, image=logo_image)
canvas.grid(row=0, column=1)

# Website, Email/Username, Password Labels
website_label = Label(text="Website:", font=("Comic Sans MS", 12))
website_label.grid(row=1, column=0)

email_label = Label(text="Email/Username:", font=("Comic Sans MS", 12))
email_label.grid(row=2, column=0)

password_label = Label(text="Password:", font=("Comic Sans MS", 12))
password_label.grid(row=3, column=0)


# Website, Email/Username, Password Entry Fields
website_entry = Entry(width=53)
website_entry.grid(row=1, column=1, columnspan=2, sticky="W")

email_entry = Entry(width=53)
email_entry.grid(row=2, column=1, columnspan=2, sticky="W")
email_entry.insert(0, "example@gmail.com")

password_entry = Entry(width=30)
password_entry.grid(row=3, column=1, sticky="W")

# Buttons
generate_button = Button(text="Generate Password", width=15, command=generate_password)
generate_button.grid(row=3, column=2, sticky="W")

add_button = Button(text="Add", width=44, command=save_credentials)
add_button.grid(row=4, column=1, columnspan=2, sticky="W")

window.mainloop()
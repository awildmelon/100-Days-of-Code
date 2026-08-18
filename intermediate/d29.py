
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

def load_credentials_file():
    file_path = os.path.join(base_path, "packages", "d29", "password_data.json")

    if not os.path.exists(file_path):
        return {}

    with open(file_path, "r") as file:
        try:
            data = json.load(file)
        except json.JSONDecodeError:
            return {}

    if isinstance(data, list):
        converted = {}
        for item in data:
            if isinstance(item, dict) and "website" in item:
                converted[item["website"]] = {
                    "email": item.get("email", ""),
                    "password": item.get("password", "")
                }
        return converted

    if isinstance(data, dict):
        return data

    return {}


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
        data = load_credentials_file()

        data[website] = {
            "email": email,
            "password": password
        }

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

# ---------------------------- SEARCH PASSWORD ------------------------------- #

def search_credentials():
    website = search_entry.get().strip()

    if not website:
        messagebox.showwarning(title="Warning", message="Please enter a website to search.")
        return

    file_path = os.path.join(base_path, "packages", "d29", "password_data.json")

    if not os.path.exists(file_path):
        messagebox.showinfo(title="Not Found", message="No saved credentials found yet.")
        return

    data = load_credentials_file()

    if website in data:
        entry = data[website]
        website_entry.delete(0, END)
        website_entry.insert(0, website)
        email_entry.delete(0, END)
        email_entry.insert(0, entry["email"])
        password_entry.delete(0, END)
        password_entry.insert(0, entry["password"])

        messagebox.showinfo(
            title="Search Result",
            message=f"Website: {website}\nEmail: {entry['email']}\nPassword: {entry['password']}"
        )
        return

    messagebox.showwarning(title="Not Found", message=f"No credentials found for {website}.")

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

search_label = Label(text="Search Website:", font=("Comic Sans MS", 12))
search_label.grid(row=5, column=0)

# Website, Email/Username, Password Entry Fields
website_entry = Entry(width=53)
website_entry.grid(row=1, column=1, columnspan=2, sticky="W")

email_entry = Entry(width=53)
email_entry.grid(row=2, column=1, columnspan=2, sticky="W")
email_entry.insert(0, "example@gmail.com")

password_entry = Entry(width=30)
password_entry.grid(row=3, column=1, sticky="W")

search_entry = Entry(width=30)
search_entry.grid(row=5, column=1, sticky="W")

# Buttons
generate_button = Button(text="Generate Password", width=15, command=generate_password)
generate_button.grid(row=3, column=2, sticky="W")

add_button = Button(text="Add", width=44, command=save_credentials)
add_button.grid(row=4, column=1, columnspan=2, sticky="W")

search_button = Button(text="Search", width=15, command=search_credentials)
search_button.grid(row=5, column=2, sticky="W")

window.mainloop()
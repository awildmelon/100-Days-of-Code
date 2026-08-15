
# Day 29 - Password Manager - 14/08/2026

from tkinter import *
from tkinter import messagebox
import os

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_credentials():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if website and email and password:
        file_path = os.path.join(base_path, "packages", "d29", "password_data.txt")
        
        with open(file_path, "a") as file:
            file.write(f"{website} | {email} | {password}\n")

        website_entry.delete(0, END)
        email_entry.delete(0, END)
        email_entry.insert(0, "example@gmail.com")
        password_entry.delete(0, END)

        messagebox.showinfo(title="Success", message="Login credentials saved successfully!")

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
generate_button = Button(text="Generate Password", width=15)
generate_button.grid(row=3, column=2, sticky="W")

add_button = Button(text="Add", width=44, command=save_credentials)
add_button.grid(row=4, column=1, columnspan=2, sticky="W")

window.mainloop()

# Day 32 - Automated Birthday Wisher - 19/08/2026

# Because this project requires using an actual email account,
# I will only be coding the logic and not actually sending any emails.

from datetime import datetime as dt
import pandas
import random
import smtplib
import os


my_email = "example@gmail.com"
password = "password"
my_name = "name"

base_path = os.path.dirname(__file__)
data_path = os.path.join(base_path, "packages", "d33")
birthdays_file = os.path.join(data_path, "birthdays.csv")

letter_files = [
    os.path.join(data_path, filename)
    for filename in os.listdir(data_path)
    if filename.startswith("letter_") and filename.endswith(".txt")
]

today = dt.now()
birthdays = pandas.read_csv(birthdays_file, skipinitialspace=True)

birthday_people = birthdays[
    (birthdays["month"] == today.month)
    & (birthdays["day"] == today.day)
]

if not birthday_people.empty:
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)

        for _, person in birthday_people.iterrows():
            letter_file = random.choice(letter_files)

            with open(letter_file, encoding="utf-8") as file:
                letter = file.read()

            letter = letter.replace("[NAME]", person["name"])
            letter = letter.replace("[RECIPIENT]", person["name"])
            letter = letter.replace("[USER]", my_name)

            message = (
                "Subject: Happy Birthday!\n"
                f"From: {my_email}\n"
                f"To: {person['email']}\n"
                "\n"
                f"{letter}"
            )

            connection.sendmail(
                from_addr=my_email,
                to_addrs=person["email"],
                msg=message,
            )

            print(f"Birthday email sent to {person['name']}")
else:
    print("No birthdays today.")
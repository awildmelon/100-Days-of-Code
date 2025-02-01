
# Day 2 - Tip Calculator - 08/01/2025

print("Welcome to the tip calculator!")
total_bill = float(input("What was the total bill? $"))
tip_percentage = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))
tip = total_bill * tip_percentage / 100
total = total_bill + tip
total_per_person = total / people
print(f"Each person should pay: ${total_per_person:.2f}")

# Day 10 - Calculator - 16/01/2025

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

continue_calculating = "y"
result = float(input("What's the first number? "))

while continue_calculating == "y":
    n1 = result
    for symbol in operations:
        print(symbol)
    operation_symbol = input("Pick an operation from the line above: ")
    n2 = float(input("What's the next number? "))
    calculation_function = operations[operation_symbol]
    result = calculation_function(n1, n2)

    print(f"{n1} {operation_symbol} {n2} = {result}")

    continue_calculating = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ").lower()

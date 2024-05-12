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
    "/": divide,
}


def calculator():
    print("Welcome to Python Calculator!")
    first_number = float(input("What is your first number?\n"))
    for symbol in operations:
        print(symbol)

    while True:
        operator = input("Pick an operator:\n")
        second_number = float(input("What is your next number?\n"))
        calculation_function = operations[operator]
        result = calculation_function(first_number, second_number)
        print(f"{first_number} {operator} {second_number} = {result}")

        should_continue = input("Type 'Y' to continue the calculation, 'R' to restart calculator, or 'N' to stop:\n").lower()
        if should_continue == "y":
            first_number = result
        elif should_continue == "r":
            calculator()
        else:
            break


calculator()
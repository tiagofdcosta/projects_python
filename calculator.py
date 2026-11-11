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

def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a number.")


def calculate():
    num1 = get_number("First Number: ")

    restart = True
    while restart == True:
        for symbols in operations:
            print(symbols)
        operation_symbols = input("Witch operation? ")
        num2 = get_number("New number: ")
        try:
            result = operations[operation_symbols](num1, num2)
        except ZeroDivisionError:
            print("You cannot divide by zero. Please try again.")
            continue
        print(f"Result: {num1} {operation_symbols} {num2} = {result}")

        choice = input(f"Continue the Operation with {result}? Yes:´y´ or No: ´n': ").lower()
        if choice == "y":
            num1 = result
        elif choice == "n":
            print("--- See you soon ---")
            restart = False


print("--- WELCOME TO THE CALCULATOR ---")
calculate()
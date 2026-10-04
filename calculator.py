import math


# -------------------------
# Mathematical functions
# -------------------------

def add_numbers(first_number, second_number):
    return first_number + second_number


def subtract_numbers(first_number, second_number):
    return first_number - second_number


def multiply_numbers(first_number, second_number):
    return first_number * second_number


def divide_numbers(first_number, second_number):
    return first_number / second_number


def power_numbers(base, exponent):
    return base ** exponent


def square_root(number):
    return math.sqrt(number)


def factorial(number):
    return math.factorial(number)


def absolute_value(number):
    return abs(number)


def sine_function(angle):
    radians = math.radians(angle)
    return math.sin(radians)


def cosine_function(angle):
    radians = math.radians(angle)
    return math.cos(radians)


def tangent_function(angle):
    if math.isclose(angle % 180, 90, abs_tol=1e-10):
        return "undefined"

    radians = math.radians(angle)
    return math.tan(radians)


def common_logarithm(number):
    if number <= 0:
        return "undefined"

    return math.log10(number)


def natural_logarithm(number):
    if number <= 0:
        return "undefined"

    return math.log(number)


def exponential_function(exponent):
    return math.exp(exponent)


def percentage(number, percentage_value):
    return number * percentage_value / 100


def reciprocal(number):
    if number == 0:
        return "undefined"

    return 1 / number


# -------------------------
# Welcome message
# -------------------------

print("=" * 75)
print("              SCIENTIFIC CALCULATOR")
print("=" * 75)
print("Welcome! This calculator can perform basic arithmetic and")
print("several advanced mathematical operations.")
print("")


# -------------------------
# Main calculator
# -------------------------

calculator_running = True

while calculator_running:

    # Display the menu
    print("\n" + "-" * 75)
    print("AVAILABLE OPERATIONS")
    print("-" * 75)

    print("1.  Addition")
    print("2.  Subtraction")
    print("3.  Multiplication")
    print("4.  Division")
    print("5.  Power")
    print("6.  Square root")
    print("7.  Factorial")
    print("8.  Absolute value")
    print("9.  Sine")
    print("10. Cosine")
    print("11. Tangent")
    print("12. Common logarithm (log₁₀)")
    print("13. Natural logarithm (ln)")
    print("14. Exponential (eˣ)")
    print("15. Percentage")
    print("16. Reciprocal")

    # Get a valid operation
    while True:
        operation = input("\nEnter your choice (1-16): ")

        if operation in (
            "1", "2", "3", "4",
            "5", "6", "7", "8",
            "9", "10", "11", "12",
            "13", "14", "15", "16"
        ):
            break

        print("Invalid choice. Please enter a number from 1 to 16.")

    # -------------------------
    # Get required inputs
    # -------------------------

    if operation == "5":

        # Get base
        while True:
            try:
                base = float(input("Enter the base: "))
                break
            except ValueError:
                print("Invalid number. Please try again.")

        # Get exponent
        while True:
            try:
                exponent = float(input("Enter the exponent: "))
                break
            except ValueError:
                print("Invalid number. Please try again.")

    elif operation == "6":

        while True:
            try:
                number = float(input("Enter the number: "))
                break
            except ValueError:
                print("Invalid number. Please try again.")

    elif operation == "7":

        while True:
            try:
                factorial_number = int(input("Enter the number: "))
                break
            except ValueError:
                print("Invalid integer. Please try again.")

    elif operation == "8":

        while True:
            try:
                absolute_number = float(input("Enter the number: "))
                break
            except ValueError:
                print("Invalid number. Please try again.")

    elif operation in ("9", "10", "11"):

        while True:
            try:
                angle = float(input("Enter the angle in degrees: "))
                break
            except ValueError:
                print("Invalid number. Please try again.")

    elif operation == "12":

        while True:
            try:
                common_logarithm_number = float(input("Enter the number: "))
                break
            except ValueError:
                print("Invalid number. Please try again.")

    elif operation == "13":

        while True:
            try:
                natural_logarithm_number = float(input("Enter the number: "))
                break
            except ValueError:
                print("Invalid number. Please try again.")

    elif operation == "14":

        while True:
            try:
                exponential_number = float(input("Enter the exponent: "))
                break
            except ValueError:
                print("Invalid number. Please try again.")

    elif operation == "15":

        while True:
            try:
                number = float(input("Enter the number: "))
                percentage_value = float(input("Enter the percentage: "))
                break
            except ValueError:
                print("Invalid number. Please try again.")

    elif operation == "16":

        while True:
            try:
                reciprocal_number = float(input("Enter the number: "))
                break
            except ValueError:
                print("Invalid number. Please try again.")

    else:

        # Get first number
        while True:
            try:
                first_number = float(input("Enter the first number: "))
                break
            except ValueError:
                print("Invalid number. Please try again.")

        # Get second number
        while True:
            try:
                second_number = float(input("Enter the second number: "))
                break
            except ValueError:
                print("Invalid number. Please try again.")

    # -------------------------
    # Perform calculation
    # -------------------------

    print("\n" + "-" * 75)

    match operation:

        case "1":
            result = add_numbers(first_number, second_number)
            print(f"Result: {result}")

        case "2":
            result = subtract_numbers(first_number, second_number)
            print(f"Result: {result}")

        case "3":
            result = multiply_numbers(first_number, second_number)
            print(f"Result: {result}")

        case "4":
            if second_number == 0:
                print("Error: Division by zero is not allowed.")
            else:
                result = divide_numbers(first_number, second_number)
                print(f"Result: {result}")

        case "5":
            result = power_numbers(base, exponent)
            print(f"Result: {result}")

        case "6":
            if number < 0:
                print("Error: Square root of a negative number is not a real number.")
            else:
                result = square_root(number)
                print(f"Result: {result}")

        case "7":
            if factorial_number < 0:
                print("Error: Factorial requires a non-negative integer.")
            else:
                result = factorial(factorial_number)
                print(f"Result: {result}")

        case "8":
            result = absolute_value(absolute_number)
            print(f"Result: {result}")

        case "9":
            result = sine_function(angle)
            print(f"Result: {result}")

        case "10":
            result = cosine_function(angle)
            print(f"Result: {result}")

        case "11":
            result = tangent_function(angle)
            print(f"Result: {result}")

        case "12":
            result = common_logarithm(common_logarithm_number)
            print(f"Result: {result}")

        case "13":
            result = natural_logarithm(natural_logarithm_number)
            print(f"Result: {result}")

        case "14":
            result = exponential_function(exponential_number)
            print(f"Result: {result}")

        case "15":
            result = percentage(number, percentage_value)
            print(f"Result: {result}")

        case "16":
            result = reciprocal(reciprocal_number)
            print(f"Result: {result}")

    print("-" * 75)

    # -------------------------
    # Continue or exit
    # -------------------------

    while True:
        continue_calculation = input(
            "\nWould you like to perform another calculation? (Yes/No): "
        ).lower()

        if continue_calculation in ("yes", "y"):
            break

        elif continue_calculation in ("no", "n"):
            calculator_running = False
            print("\nThank you for using the Scientific Calculator!")
            print("Have a great day!")
            break

        else:
            print("Invalid response. Please enter Yes or No.")


print("\nProgram closed.")
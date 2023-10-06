# Function to perform addition
def add(x, y):
    return x + y

# Function to perform subtraction
def subtract(x, y):
    return x - y

# Function to perform multiplication
def multiply(x, y):
    return x * y

# Function to perform division
def divide(x, y):
    if y == 0:
        return "Cannot divide by zero"
    return x / y

# Main program
while True:
    # Prompt the user for input
    print("Options:")
    print("Enter 'add' for addition")
    print("Enter 'subtract' for subtraction")
    print("Enter 'multiply' for multiplication")
    print("Enter 'divide' for division")
    print("Enter 'quit' to end the program")

    user_input = input(": ")

    # Check for the quit command
    if user_input == "quit":
        break

    # Check for valid operations
    if user_input not in ("add", "subtract", "multiply", "divide"):
        print("Invalid input")
        continue

    # Prompt the user for numbers
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    # Perform the selected operation
    if user_input == "add":
        result = add(num1, num2)
    elif user_input == "subtract":
        result = subtract(num1, num2)
    elif user_input == "multiply":
        result = multiply(num1, num2)
    elif user_input == "divide":
        result = divide(num1, num2)

    # Display the result
    print("Result: ", result)

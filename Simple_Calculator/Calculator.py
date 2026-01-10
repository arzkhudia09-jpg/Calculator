#Operations

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b    

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b


#Functioning
while True:
    name = "=== Simple Calculator ==="

    num1 = int(input("Enter first number: "))

    operation = input("Choose an operation (+, -, *, /): ")

    num2 = int(input("Enter second number: "))

    if operation == "+":
        print(f"{num1} + {num2} = {add(num1, num2)}")
    elif operation == "-":
        print(f"{num1} - {num2} = {subtract(num1, num2)}")
    elif operation == "*":
        print(f"{num1} * {num2} = {multiply(num1, num2)}")
    elif operation == "/":
        try:
            print(f"{num1} / {num2} = {divide(num1, num2)}")
        except ValueError as e:
            print(e)
    choice = input("Do you want to perform another calculation? (y/n): ")
    if choice.lower() != 'y':
        print("Thank you for using the calculator. Goodbye!")
        break
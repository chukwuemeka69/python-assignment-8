#! /usr/bin/python3
# script5.py

from calculator import add, subtract, multiply, divide

def get_user_input():
    """Prompt user for two numbers and return them as floats."""
    try:
        a = float(input("Enter the first number: "))
        b = float(input("Enter the second number: "))
        return a, b
    except ValueError:
        print("Invalid input. Please enter a number.")
        return get_user_input()

def main():
    print("Choose an operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    
    operation = input("Enter the number (1/2/3/4): ")

    a, b = get_user_input()

    if operation == '1':
        print(f"{a} + {b} = {add(a, b)}")
    elif operation == '2':
        print(f"{a} - {b} = {subtract(a, b)}")
    elif operation == '3':
        print(f"{a} * {b} = {multiply(a, b)}")
    elif operation == '4':
        if b == 0:
            print("Cannot divide by zero!")
        else:
            print(f"{a} / {b} = {divide(a, b)}")
    else:
        print("Invalid operation selected.")

if __name__ == "__main__":
    main()

# 📘 Lecture 12 – Return Statement & Calculator
# Urdu IT Academy | Python for Beginners

# ----------------------------------------
# 🔁 Area of a Circle (Using return)
# ----------------------------------------

def area(radius):
    return 3.14 * radius * radius

radius = int(input("Enter the radius: "))
result = area(radius)
print("Area is", result)

# ----------------------------------------
# 🔁 Square of a Number
# ----------------------------------------

def find_square(num):
    return num * num

square = find_square(3)
print("Square is", square)

# ----------------------------------------
# 🔁 Recursive Factorial Function
# ----------------------------------------

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

n = int(input("Enter a number: "))
if n < 0:
    print("Factorial does not exist for negative numbers")
else:
    print(f"The factorial of {n} is {factorial(n)}")

# ----------------------------------------
# 🔁 Fibonacci Series using Recursion
# ----------------------------------------

def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

num_terms = int(input("Enter the number of terms: "))
for i in range(num_terms):
    print(fibonacci(i))

# ----------------------------------------
# 📏 Square Root using math module
# ----------------------------------------

import math

def find_square_root(number):
    return math.sqrt(number)

num = float(input("Enter a number: "))
result = find_square_root(num)
print(f"The square root of {num} is {result}")

# ----------------------------------------
# 🧮 Calculator using return statements
# ----------------------------------------

def addition(a, b):
    return a + b

def subtraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: Cannot divide by zero!"

while True:
    print("\nSimple Calculator")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    choice = input("Enter your choice (1/2/3/4): ")

    if choice in ('1', '2', '3', '4'):
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))

        if choice == '1':
            result = addition(a, b)
            print(f"{a} + {b} = {result}")
        elif choice == '2':
            result = subtraction(a, b)
            print(f"{a} - {b} = {result}")
        elif choice == '3':
            result = multiplication(a, b)
            print(f"{a} * {b} = {result}")
        elif choice == '4':
            result = division(a, b)
            print(f"{a} / {b} = {result}")
    else:
        print("Invalid choice! Please enter 1, 2, 3, or 4.")

    again = input("Do you want to do another calculation? (yes/no): ")
    if again.lower() != 'yes':
        print("Goodbye!")
        break

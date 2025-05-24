# 📘 Lecture 11 – Functions in Python
# Urdu IT Academy | Python for Beginners

# ----------------------------------------
# 🧠 Function Example 1 – Simple Function
# ----------------------------------------

def hello():
    print("Hello, world")

print("Hi")
hello()

# ----------------------------------------
# 📏 Area and Perimeter of Rectangle (No Parameters)
# ----------------------------------------

def area():
    length = int(input("Enter length of the rectangle: "))
    width = int(input("Enter width of the rectangle: "))
    result = length * width
    print("Area of rectangle is", result)

def peri():
    length = int(input("Enter length of the rectangle: "))
    width = int(input("Enter width of the rectangle: "))
    result = 2 * (length + width)
    print("Perimeter of rectangle is", result)

area()
peri()

# ----------------------------------------
# ➕ Sum and Average of Three Numbers (With Parameters)
# ----------------------------------------

def sum(a, b, c):
    total = a + b + c
    print("Sum:", total)

def average(a, b, c):
    avg = (a + b + c) / 3
    print("Average:", avg)

# User input
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))

# Function calls
sum(num1, num2, num3)
average(num1, num2, num3)

# ----------------------------------------
# 🧮 HW Example: Area and Perimeter using Parameterized Functions
# ----------------------------------------

def find_area(length, width):
    area = length * width
    print("Area of rectangle =", area)

def find_perimeter(length, width):
    perimeter = 2 * (length + width)
    print("Perimeter of rectangle =", perimeter)

# Input from user
length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))

# Function calls
find_area(length, width)
find_perimeter(length, width)

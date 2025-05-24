# 📘 Lecture 1 & 2 – Introduction to Python & Basic Math Programs
# Urdu IT Academy | Python for Beginners

# -------------------------------
# Program 1: Basic User Input
# -------------------------------

print("What is your name?")
name = input()

print("Where are you from?")
place = input()

print("What is your hobby?")
hobby = input()

print("Hi", name)
print("You are from", place)
print("Your hobby is", hobby)

# -------------------------------
# Program 2: Sum of Two Numbers
# -------------------------------

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
total = num1 + num2

print("The sum of", num1, "and", num2, "is:", total)

# ---------------------------------------------
# Program 3: Area and Perimeter of a Rectangle
# ---------------------------------------------

length = int(input("What is the length? "))
width = int(input("What is the width? "))

area = length * width
perimeter = 2 * (length + width)

print("Area is", area)
print("Perimeter is", perimeter)

# ----------------------------------------
# Program 4: Calculate Percentage of Marks
# ----------------------------------------

total_marks = int(input("Enter the total marks: "))
marks_obtained = int(input("Enter the marks obtained: "))

percentage = (marks_obtained / total_marks) * 100
print("Percentage:", percentage, "%")

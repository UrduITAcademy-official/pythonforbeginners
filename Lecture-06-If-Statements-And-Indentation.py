# 📘 Lecture 6 – If Statements & Indentation
# Urdu IT Academy | Python for Beginners

# -----------------------------------
# 🔹 Simple if Statement
# -----------------------------------

num = 5
if num == 5:
    print("The number is 5")

num = 7
if num > 0:
    print("The number is positive")

# -----------------------------------
# 🔹 if-else Statement
# -----------------------------------

num = int(input("Enter a number: "))
if num > 0:
    print("It's a positive number")
else:
    print("It's a negative number")

# -----------------------------------
# 🔹 if-else with Strings
# -----------------------------------

name = input("Enter your name: ")
if name == "sara":
    print("Hi Sara")
else:
    print("I don't know who you are")

# -----------------------------------
# 🔹 if-elif-else Chain
# -----------------------------------

day_number = int(input("Enter a number from 1 to 7: "))

if day_number == 1:
    print("Monday")
elif day_number == 2:
    print("Tuesday")
elif day_number == 3:
    print("Wednesday")
elif day_number == 4:
    print("Thursday")
elif day_number == 5:
    print("Friday")
elif day_number == 6:
    print("Saturday")
elif day_number == 7:
    print("Sunday")
else:
    print("Invalid input! Please enter a number from 1 to 7.")

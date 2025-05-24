# 📘 Lecture 9 – For Loops in Python
# Urdu IT Academy | Python for Beginners

# --------------------------------------
# 🔁 Looping through a List
# --------------------------------------

colours = ["red", "green", "blue"]
for x in colours:
    print(x)

# --------------------------------------
# 🔁 Looping through a String
# --------------------------------------

for x in "hello":
    print(x)

# --------------------------------------
# 🔁 Looping through a Range (0 to 4)
# --------------------------------------

for x in range(5):
    print(x)

# --------------------------------------
# 🔁 Print numbers in a user-defined range
# --------------------------------------

start = int(input("Enter starting number: "))
limit = int(input("Enter limit: "))

for x in range(start, limit):
    print(x)

# --------------------------------------
# 🔁 Even numbers from 2 to 20
# --------------------------------------

for x in range(2, 21, 2):
    print(x)

# --------------------------------------
# 🔁 Multiples of 5 from 5 to 50
# --------------------------------------

for x in range(5, 51, 5):
    print(x)

# --------------------------------------
# 🔁 Countdown from 10 to 1
# --------------------------------------

for i in range(10, 0, -1):
    print(i)

# --------------------------------------
# 🔁 Print odd numbers up to a limit
# --------------------------------------

limit = int(input("Enter limit: "))
for x in range(1, limit, 2):
    print(x)

# --------------------------------------
# 🔁 Multiplication Table of a Number
# --------------------------------------

num = int(input("Enter a number: "))
for i in range(1, 11):
    print(i, "x", num, "=", i * num)

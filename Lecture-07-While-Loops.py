# 📘 Lecture 7 – While Loops in Python
# Urdu IT Academy | Python for Beginners

# -----------------------------------------
# 🔁 Print "Hello World" 10 Times
# -----------------------------------------

i = 0
while i < 10:
    print("hello world")
    i = i + 1

# -----------------------------------------
# 🔁 Print Numbers from 1 to 10
# -----------------------------------------

i = 1
while i <= 10:
    print(i)
    i = i + 1

# -----------------------------------------
# 🔁 Print Table of 5 up to 50
# -----------------------------------------

n = 5
while n <= 50:
    print(n)
    n = n + 5

# -----------------------------------------
# 🔁 Multiplication Table of Any Number
# -----------------------------------------

n = int(input("Enter the number: "))
i = 1
while i <= 10:
    print(i, 'x', n, '=', i * n)
    i = i + 1

# -----------------------------------------
# 🔁 Print Odd Numbers in a Range
# -----------------------------------------

start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))

print("Odd numbers between", start, "and", end, "are:")
while start <= end:
    if start % 2 != 0:
        print(start)
    start += 1

# -----------------------------------------
# 🔁 Sum of Even Numbers in a Range
# -----------------------------------------

start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))
sum_even = 0

while start <= end:
    if start % 2 == 0:
        sum_even += start
    start += 1

print("Sum of even numbers in the given range is:", sum_even)

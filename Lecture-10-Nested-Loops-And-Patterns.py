# 📘 Lecture 10 – Nested Loops & Pattern Printing
# Urdu IT Academy | Python for Beginners

# ------------------------------------------
# ⭐ Star Pattern – Right-Angled Triangle
# ------------------------------------------

rows = int(input("Enter the number of rows: "))
for i in range(rows):
    for j in range(i + 1):
        print("*", end=' ')
    print()

# ------------------------------------------
# 🔢 Number Pattern – Repeated Row Numbers
# ------------------------------------------

rows = int(input("Enter the number of rows: "))
for i in range(1, rows + 1):
    for j in range(i):
        print(i, end=' ')
    print()

# ------------------------------------------
# 🔢 Number Pattern – Increasing Sequence
# ------------------------------------------

rows = int(input("Enter the number of rows: "))
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print(j, end=' ')
    print()

# ------------------------------------------
# 🔁 Reverse Number Pattern
# ------------------------------------------

rows = int(input("Enter the number of rows: "))
for i in range(rows, 0, -1):
    for j in range(i):
        print(i, end=' ')
    print()

# ------------------------------------------
# 🔁 Multiplication Table Pattern
# ------------------------------------------

rows = int(input("Enter the number of rows: "))
for i in range(1, rows):
    for j in range(1, i + 1):
        print(i * j, end=' ')
    print()

# ------------------------------------------
# 🔁 While Loop Number Pattern
# Odd number series using while inside nested loop
# ------------------------------------------

rows = int(input("Enter the number of rows: "))
i = 1
while i <= rows:
    j = 1
    while j <= i:
        print((i * 2 - 1), end=' ')
        j += 1
    i += 1
    print()

# ------------------------------------------
# ⭐ Reverse Star Pattern
# ------------------------------------------

rows = int(input("Enter the number of rows: "))
for i in range(rows, 0, -1):
    for j in range(i):
        print("*", end=' ')
    print()

# ------------------------------------------
# 🔢 Even Number Pattern
# ------------------------------------------

for i in range(1, 6):
    for j in range(i):
        print(2 * i, end=' ')
    print()

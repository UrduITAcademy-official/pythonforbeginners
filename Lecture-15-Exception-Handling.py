# 📘 Lecture 15 – Exception Handling in Python
# Urdu IT Academy | Python for Beginners

# ----------------------------------------
# ❌ Example: ValueError
# ----------------------------------------

try:
    number = int("abc")
except ValueError:
    print("Error: cannot convert to an integer")

# ----------------------------------------
# ➗ Example: ZeroDivisionError
# ----------------------------------------

try:
    number = int(input("Enter a number: "))
    result = 10 / number
    print("Result:", result)
except ValueError:
    print("Error: Please enter a valid number")
except ZeroDivisionError:
    print("Math Error: Cannot divide by zero")

# ----------------------------------------
# ✅ Using else and finally
# ----------------------------------------

try:
    result = 10 / 2
except ZeroDivisionError:
    print("Math Error: Cannot divide by zero")
else:
    print("Division successful:", result)

# Example with file handling
try:
    with open('samp111.txt', 'r') as file:
        content = file.read()
except FileNotFoundError:
    print("File not found")
finally:
    print("Execution completed")

# ----------------------------------------
# 🚫 Raising a custom exception
# ----------------------------------------

age = -6
if age < 0:
    raise ValueError("Age cannot be negative")

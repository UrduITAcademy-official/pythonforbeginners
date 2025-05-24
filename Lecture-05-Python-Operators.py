# 📘 Lecture 5 – All Python Operators Explained
# Urdu IT Academy | Python for Beginners

# ------------------------------
# 🔢 Arithmetic Operators
# ------------------------------
print("3 + 4 =", 3 + 4)    # Addition
print("3 - 4 =", 3 - 4)    # Subtraction
print("3 * 4 =", 3 * 4)    # Multiplication
print("3 / 4 =", 3 / 4)    # Division
print("3 // 4 =", 3 // 4)  # Floor Division
print("3 ** 4 =", 3 ** 4)  # Exponentiation (Power)

# ------------------------------
# 🔍 Comparison Operators
# ------------------------------
a = 5
b = 7

print("a > b =", a > b)
print("a < b =", a < b)
print("a == b =", a == b)
print("a != b =", a != b)
print("a >= b =", a >= b)
print("a <= b =", a <= b)

# ------------------------------
# 🔁 Logical Operators
# ------------------------------
a = True
b = False

print("a and b =", a and b)
print("a or b =", a or b)
print("not a =", not a)
print("not b =", not b)

# ------------------------------
# ⚙️ Bitwise Operators
# ------------------------------
a = 5  # 0101
b = 3  # 0011

print("a & b =", a & b)     # AND
print("a | b =", a | b)     # OR
print("a ^ b =", a ^ b)     # XOR
print("~a =", ~a)           # NOT
print("a << 1 =", a << 1)   # Left Shift
print("a >> 1 =", a >> 1)   # Right Shift

# ------------------------------
# 📝 Assignment Operators
# ------------------------------
a = 10
print("Initial a =", a)

a += 5
print("a += 5 →", a)

a -= 3
print("a -= 3 →", a)

a *= 2
print("a *= 2 →", a)

a /= 4
print("a /= 4 →", a)

a %= 3
print("a %= 3 →", a)

a = 5
a **= 2
print("a **= 2 →", a)

a //= 3
print("a //= 3 →", a)

# ------------------------------
# 🆔 Identity Operators
# ------------------------------
a = 5
b = 5
c = [1, 2, 3]
d = [1, 2, 3]

print("a is b =", a is b)       # True
print("c is d =", c is d)       # False
print("a is not b =", a is not b)
print("c is not d =", c is not d)

# ------------------------------
# 📦 Membership Operators
# ------------------------------
fruits = ['apple', 'banana', 'cherry']

print("'apple' in fruits =", 'apple' in fruits)
print("'mango' in fruits =", 'mango' in fruits)
print("'banana' not in fruits

# 📘 Lecture 4 – Data Type Conversion & String Operations
# Urdu IT Academy | Python for Beginners

# --------------------------------------
# 🔁 Data Type Conversions in Python
# --------------------------------------

# Float to Integer
a = int(5.5)
print(a)
print("Type of a:", type(a))

# Integer to String
a = str(25)
print(a)
print("Type of a:", type(a))

# Integer to Float
a = float(12)
print(a)
print("Type of a:", type(a))

# Integer to Complex
a = complex(5)
print(a)
print("Type of a:", type(a))


# --------------------------------------
# 🧵 String Operations in Python
# --------------------------------------

text = "good morning"

# Concatenation
greeting = text + " everyone"
print("Concatenation:", greeting)

# Repetition
repeated = text * 2
print("Repetition:", repeated)

# Slicing
slice_example = text[0:4]  # 'good'
print("Slice (0:4):", slice_example)

# Range Slice
range_slice = text[5:]  # from index 5 to end
print("Range Slice (5:):", range_slice)

# Membership Test
is_present = "good" in text
print("'good' in text:", is_present)

not_present = "night" not in text
print("'night' not in text:", not_present)

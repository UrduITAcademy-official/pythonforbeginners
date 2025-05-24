# 📘 Lecture 16 – File Handling in Python
# Urdu IT Academy | Python for Beginners

# ----------------------------------------
# ✏️ Create and Write to a File
# ----------------------------------------

file = open("example.txt", "w")  # Open file in write mode
file.write("Hello, students!\n")
file.write("Welcome to Python file handling.")
file.close()

print("File written successfully!")

# ----------------------------------------
# 📖 Read from a File
# ----------------------------------------

file = open("example.txt", "r")
content = file.read()
print("File content:\n", content)
file.close()

# ----------------------------------------
# ➕ Append to a File
# ----------------------------------------

file = open("example.txt", "a")
file.write("\nKeep learning and coding!")
file.close()

print("Content appended successfully!")

# ----------------------------------------
# ✅ Using 'with' Statement (Recommended)
# ----------------------------------------

with open("example.txt", "r") as file:
    content = file.read()
    print("Reading with 'with' statement:\n", content)

# ----------------------------------------
# 📓 Simple Diary App
# ----------------------------------------

def add_entry():
    entry = input("Enter your diary entry:\n")
    with open("diary.txt", "a") as file:
        file.write(entry + "\n")
    print("Entry added successfully.\n")

def view_entries():
    with open("diary.txt", "r") as file:
        print("\nYour Diary entries:")
        print(file.read())

while True:
    print("\nDiary Menu:")
    print("1. Add New Entry")
    print("2. View All Entries")
    print("3. Exit")
    
    choice = input("Enter your choice (1/2/3): ")
    
    if choice == "1":
        add_entry()
    elif choice == "2":
        view_entries()
    elif choice == "3":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")

# ----------------------------------------
# 📂 Copy contents from one file to another
# ----------------------------------------

with open("source.txt", "r") as source_file:
    with open("destination.txt", "w") as dest_file:
        for line in source_file:
            dest_file.write(line)

print("File copied successfully.")

# ----------------------------------------
# ➕ Sum of Numbers from a File
# (Assumes file contains one number per line)
# ----------------------------------------

with open("numbers.txt", "r") as file:
    total = 0
    for line in file:
        total += int(line.strip())

print("Sum of numbers:", total)

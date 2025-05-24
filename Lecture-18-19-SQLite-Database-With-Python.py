# 📘 Lecture 18 & 19 – SQLite Database Integration with Python
# Urdu IT Academy | Python for Beginners

import sqlite3

# ----------------------------------------
# 🔗 Connect to SQLite database
# ----------------------------------------

conn = sqlite3.connect("example.db")  # Creates file if it doesn't exist
cursor = conn.cursor()
print("Database connected successfully!")

# ----------------------------------------
# 🏗️ Create Table (if not exists)
# ----------------------------------------

cursor.execute('''
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY,
    name TEXT,
    age INTEGER,
    grade TEXT
)
''')
print("Table 'students' created successfully!")

# ----------------------------------------
# 🛠️ Alter Table – Add new column
# (Run only once or handle with try-except to avoid duplicate error)
# ----------------------------------------

try:
    cursor.execute("ALTER TABLE students ADD COLUMN email TEXT")
    print("Column 'email' added successfully!")
except sqlite3.OperationalError:
    print("Column 'email' already exists!")

# ----------------------------------------
# ❌ Drop Table (Uncomment if needed)
# ----------------------------------------

# cursor.execute("DROP TABLE students")
# print("Table 'students' dropped successfully!")

# ----------------------------------------
# ➕ Insert Data into Table
# ----------------------------------------

cursor.execute('''
INSERT INTO students (name, age, grade)
VALUES ('Alice', 14, '8th')
''')
conn.commit()
print("Data inserted successfully!")

# ----------------------------------------
# 🔍 Select All Records
# ----------------------------------------

cursor.execute("SELECT * FROM students")
rows = cursor.fetchall()
print("\nAll Students:")
for row in rows:
    print(row)

# ----------------------------------------
# 🔍 Select by Condition (e.g., name = 'Bob')
# ----------------------------------------

cursor.execute("SELECT * FROM students WHERE name = 'Bob'")
student = cursor.fetchone()

if student:
    print("\nDetails of student named Bob:", student)
else:
    print("\nNo student named Bob found.")

# ----------------------------------------
# ✏️ Update Data
# ----------------------------------------

cursor.execute('''
UPDATE students
SET grade = '8th Grade'
WHERE id = 3
''')
conn.commit()
print(f"\nUpdated {cursor.rowcount} row(s) successfully!")

# ----------------------------------------
# 🗑️ Delete Data
# ----------------------------------------

cursor.execute('''
DELETE FROM students
WHERE id = 3
''')
conn.commit()
print(f"Deleted {cursor.rowcount} row(s) successfully!")

# ----------------------------------------
# ✅ Final Cleanup
# ----------------------------------------

conn.close()
print("\nDatabase connection closed.")

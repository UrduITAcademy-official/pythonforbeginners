# 📘 Lecture 17 – Object-Oriented Programming (OOP)
# Urdu IT Academy | Python for Beginners

# ----------------------------------------
# 🔹 Classes and Objects
# ----------------------------------------

class Robot:
    def __init__(self, name, color):
        self.name = name
        self.color = color

my_robot = Robot("RoboX", "Silver")
print(my_robot.name)

class Robot:
    def talk(self):
        print("Hello, I am a robot")

robot = Robot()
robot.talk()

# ----------------------------------------
# 🔐 Encapsulation
# ----------------------------------------

class Car:
    def __init__(self, make, model, color):
        self.__make = make
        self.__model = model
        self.__color = color

    def get_make(self):
        return self.__make

car1 = Car("Toyota", "Corolla", "Red")
print(car1.get_make())

# ----------------------------------------
# 🧬 Inheritance – Single
# ----------------------------------------

class Animal:
    def eat(self):
        print("This animal eats food")

class Dog(Animal):
    def bark(self):
        print("Dog barks")

d = Dog()
d.eat()
d.bark()

# ----------------------------------------
# 🧬 Inheritance – Multiple
# ----------------------------------------

class Engine:
    def start(self):
        print("This engine starts")

class Wheels:
    def rotate(self):
        print("Wheels rotate")

class Car(Engine, Wheels):
    def drive(self):
        print("The car drives")

c = Car()
c.start()
c.drive()
c.rotate()

# ----------------------------------------
# 🧬 Inheritance – Multi-level
# ----------------------------------------

class Animal:
    def eat(self):
        print("This animal eats food")

class Mammal(Animal):
    def walk(self):
        print("This mammal walks")

class Dog(Mammal):
    def bark(self):
        print("Dog barks")

d = Dog()
d.eat()
d.walk()
d.bark()

# ----------------------------------------
# 🔼 Using super() to Access Parent Constructor
# ----------------------------------------

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")

class Employee(Person):
    def __init__(self, name, age, salary):
        super().__init__(name, age)
        self.salary = salary

    def display(self):
        print(f"Salary: {self.salary}")

e = Employee("Riya", 30, 300000)
e.display()

# ----------------------------------------
# 🔁 Polymorphism (Same function, different behavior)
# ----------------------------------------

class Animal:
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        return "Woof"

class Cat(Animal):
    def make_sound(self):
        return "Meow"

class Cow(Animal):
    def make_sound(self):
        return "Moo"

def sound(animal):
    print(animal.make_sound())

sound(Dog())
sound(Cat())
sound(Cow())

# ----------------------------------------
# 🧼 Abstraction using ABC
# ----------------------------------------

from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        return "Woof"

class Cat(Animal):
    def make_sound(self):
        return "Meow"

animals = [Dog(), Cat()]
for a in animals:
    print(a.make_sound())

# ----------------------------------------
# 📚 Mini Project: Library Management System
# ----------------------------------------

class Library:
    def __init__(self):
        self.books = []

    def addbook(self, book):
        self.books.append(book)
        print(f"{book} has been added")

    def borrowbook(self, book):
        if book in self.books:
            self.books.remove(book)
            print(f"{book} borrowed")
        else:
            print(f"{book} not available")

    def returnbook(self, book):
        self.books.append(book)
        print(f"{book} returned")

lib = Library()
lib.addbook("math")
lib.addbook("coding")
lib.borrowbook("math")
lib.returnbook("math")

# HW Version of Library with class Book

class Book:
    def __init__(self, title, author, copies_available):
        self.title = title
        self.author = author
        self.copies_available = copies_available

    def borrow_book(self):
        if self.copies_available > 0:
            self.copies_available -= 1
            print(f"You have successfully borrowed '{self.title}'.")
        else:
            print(f"Sorry, '{self.title}' is currently unavailable.")

    def return_book(self):
        self.copies_available += 1
        print(f"Thank you for returning '{self.title}'.")

def display_books(books):
    print("\nAvailable Books:")
    for i, book in enumerate(books):
        print(f"{i + 1}. {book.title} by {book.author} (Available: {book.copies_available})")

library = [
    Book("The Great Gatsby", "F. Scott Fitzgerald", 3),
    Book("To Kill a Mockingbird", "Harper Lee", 2),
    Book("1984", "George Orwell", 4),
    Book("Pride and Prejudice", "Jane Austen", 1)
]

while True:
    print("\nLibrary Management System")
    print("1. Display books")
    print("2. Borrow a book")
    print("3. Return a book")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        display_books(library)
    elif choice == "2":
        display_books(library)
        book_choice = int(input("Enter the number of the book you want to borrow: ")) - 1
        if 0 <= book_choice < len(library):
            library[book_choice].borrow_book()
        else:
            print("Invalid choice.")
    elif choice == "3":
        display_books(library)
        book_choice = int(input("Enter the number of the book you want to return: ")) - 1
        if 0 <= book_choice < len(library):
            library[book_choice].return_book()
        else:
            print("Invalid choice.")
    elif choice == "4":
        print("Thank you for using the Library Management System. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")

# ----------------------------------------
# 📋 Mini Project: Student Report Card
# ----------------------------------------

class Student:
    def __init__(self, name, roll_number, marks):
        self.name = name
        self.roll_number = roll_number
        self.marks = marks  # Dictionary

    def calculate_total(self):
        return sum(self.marks.values())

    def calculate_average(self):
        return self.calculate_total() / len(self.marks)

    def grade(self):
        avg = self.calculate_average()
        if avg >= 80:
            return "A"
        elif 60 <= avg < 80:
            return "B"
        elif 50 <= avg < 60:
            return "C"
        elif 35 <= avg < 50:
            return "D"
        else:
            return "F"

def display_student_report(students):
    print("\nStudent Report Card")
    print("*" * 50)
    for student in students:
        total = student.calculate_total()
        average = student.calculate_average()
        student_grade = student.grade()
        print(f"Name: {student.name}")
        print(f"Roll Number: {student.roll_number}")
        print(f"Total Marks: {total}")
        print(f"Average Marks: {average:.2f}")
        print(f"Grade: {student_grade}")
        print("-" * 50)

students = [
    Student("Alice", 101, {"Math": 85, "Science": 90, "English": 78}),
    Student("Bob", 102, {"Math": 72, "Science": 68, "English": 75}),
    Student("Charlie", 103, {"Math": 55, "Science": 60, "English": 58}),
]

display_student_report(students)

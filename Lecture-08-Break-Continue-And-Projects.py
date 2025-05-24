# 📘 Lecture 8 – While Loop with break, continue, and Mini Projects
# Urdu IT Academy | Python for Beginners

# ------------------------------------------
# 🔁 while loop with else
# ------------------------------------------

i = 0
while i < 3:
    print('Inside while')
    i += 1
else:
    print('Inside else')

# ------------------------------------------
# 🔓 break statement in a loop
# ------------------------------------------

x = 0
while x < 5:
    print(x)
    if x == 3:
        break
    x = x + 1

# ------------------------------------------
# 🔐 Password Checker with break
# ------------------------------------------

correct_password = "secure123"
while True:
    password = input("Enter your password: ")
    if password == correct_password:
        print("Access granted.")
        break
    else:
        print("Incorrect password. Try again.")

# ------------------------------------------
# 🔁 continue statement in while loop
# ------------------------------------------

x = 0
while x < 5:
    x = x + 1
    if x == 3:
        continue
    print(x)

# ------------------------------------------
# 🧵 Loop through word and skip 'e' and 's'
# ------------------------------------------

word = "letters"
for letter in word:
    if letter == 'e' or letter == 's':
        continue
    print(letter)

# ------------------------------------------
# 🧪 Skip prime numbers using continue
# ------------------------------------------

number = 1
while number <= 20:
    is_prime = True
    i = 2
    while i < number:
        if number % i == 0:
            is_prime = False
            break
        i += 1
    if is_prime and number > 1:
        number += 1
        continue
    print(number)
    number += 1

# ------------------------------------------
# 🎮 Math Quiz (ends on wrong answer)
# ------------------------------------------

import random

print("Welcome to the Math Quiz!")
print("Keep answering correctly to continue.")
print("The quiz ends if you get one wrong.\n")

while True:
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    correct_answer = num1 * num2

    print(f"What is {num1} x {num2}? ")
    user_answer = int(input())

    if user_answer == correct_answer:
        print("Correct!\n")
    else:
        print(f"Wrong! The correct answer was {correct_answer}. Game over!")
        break

# ------------------------------------------
# 🔢 Number Guessing Game
# ------------------------------------------

secret_number = random.randint(1, 100)
attempts = 0

print("Welcome to the Guessing Game!")
print("I'm thinking of a number between 1 and 100.\n")

while True:
    guess = int(input("Enter your guess: "))
    attempts += 1

    if guess < secret_number:
        print("Too low! Try again.\n")
    elif guess > secret_number:
        print("Too high! Try again.\n")
    else:
        print(f"Congratulations! You guessed it right in {attempts} attempts!")
        break

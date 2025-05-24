# 📘 Lecture 13 – Introduction to Turtle Graphics
# Urdu IT Academy | Python for Beginners

import turtle

# -----------------------------------------
# 🟠 Draw a Circle
# -----------------------------------------

screen = turtle.Screen()
t = turtle.Turtle()
t.color("red")
t.pensize(10)
t.circle(50)

# -----------------------------------------
# 🟥 Draw a Square (manual)
# -----------------------------------------

t = turtle.Turtle()
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)

# -----------------------------------------
# 🔁 Draw a Square using for loop
# -----------------------------------------

t = turtle.Turtle()
t.color("pink")
for i in range(4):
    t.forward(100)
    t.right(90)

# -----------------------------------------
# 🌀 Draw a Square Pattern
# -----------------------------------------

t = turtle.Turtle()
t.color("red")
t.speed(30)
for i in range(25):
    for j in range(4):
        t.forward(100)
        t.right(90)
    t.right(15)

# -----------------------------------------
# 🌈 Draw Multi-colored Squares
# -----------------------------------------

t = turtle.Turtle()
t.speed(30)
colours = ['red', 'blue', 'pink', 'green']
for color in colours:
    t.color(color)
    for j in range(4):
        t.forward(10)
        t.right(90)
    t.penup()
    t.forward(30)
    t.pendown()

# -----------------------------------------
# ⬠ Draw a Polygon using a Function
# -----------------------------------------

def draw_polygon(sides, length):
    angle = 360 / sides
    for j in range(sides):
        t.forward(length)
        t.right(angle)

t = turtle.Turtle()
draw_polygon(5, 100)

# -----------------------------------------
# 🔺 HW – Triangle Pattern
# -----------------------------------------

t = turtle.Turtle()
t.color("red")
for i in range(25):
    for j in range(3):
        t.forward(80)
        t.right(120)
    t.right(15)

# -----------------------------------------
# 🏠 HW – Draw a Simple House
# -----------------------------------------

t = turtle.Turtle()
screen = turtle.Screen()

# Draw triangle roof
t.fillcolor("red")
t.begin_fill()
for i in range(3):
    t.forward(90)
    t.left(120)
t.end_fill()

# Draw square house base
def sq(size):
    t.begin_fill()
    for i in range(4):
        t.forward(size)
        t.left(90)
    t.end_fill()

t.fillcolor("green")
sq(90)

# Draw windows
t.penup()
t.goto(20, -20)
t.pendown()
t.fillcolor("blue")
sq(20)

t.penup()
t.goto(55, -20)
t.pendown()
sq(20)

# Draw door
t.penup()
t.goto(35, -55)
t.pendown()
sq(30)

screen.mainloop()

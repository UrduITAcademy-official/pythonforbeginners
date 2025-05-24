# 📘 Lecture 14 – Turtle Mini Games
# Urdu IT Academy | Python for Beginners

import turtle
import random
import time

# ------------------------------------------
# 🎯 Catch the Turtle Game
# ------------------------------------------

screen = turtle.Screen()
screen.title("Catch the Turtle Game")
screen.bgcolor("lightblue")
screen.setup(width=600, height=600)

player_turtle = turtle.Turtle()
player_turtle.shape("turtle")
player_turtle.color("green")
player_turtle.penup()

score = 0
start_time = time.time()

score_display = turtle.Turtle()
score_display.hideturtle()
score_display.penup()
score_display.goto(0, 260)
score_display.write("Score: 0", align="center", font=("Arial", 20, "bold"))

def update_score():
    score_display.clear()
    score_display.write(f"Score: {score}", align="center", font=("Arial", 24, "bold"))

def move_turtle():
    x = random.randint(-250, 250)
    y = random.randint(-250, 250)
    player_turtle.goto(x, y)
    screen.ontimer(move_turtle, 2000)

def turtle_caught(x, y):
    global score
    if time.time() - start_time < 30:
        score += 1
        update_score()
        move_turtle()
    else:
        score_display.goto(0, 0)
        score_display.write("GAME OVER", align="center", font=("Arial", 24, "bold"))
        player_turtle.hideturtle()

player_turtle.onclick(turtle_caught)
move_turtle()
screen.mainloop()

# ------------------------------------------
# 🐢 Turtle Racing Game
# ------------------------------------------

screen = turtle.Screen()
screen.title("Turtle Race")
screen.bgcolor("lightgreen")
screen.setup(width=600, height=400)

# Player turtle
player = turtle.Turtle()
player.shape("turtle")
player.color("blue")
player.penup()
player.goto(-250, -50)

# Opponent turtle
opponent = turtle.Turtle()
opponent.shape("turtle")
opponent.color("red")
opponent.penup()
opponent.goto(-250, 50)

# Finish line
finish_line = turtle.Turtle()
finish_line.hideturtle()
finish_line.penup()
finish_line.goto(200, 100)
finish_line.right(90)
finish_line.pendown()
finish_line.forward(200)

def move_player():
    player.forward(20)

def move_opponent():
    opponent.forward(random.randint(0, 3))

def check_winner():
    if player.xcor() >= 200:
        screen.textinput("Game Over", "You won!")
        screen.bye()
    elif opponent.xcor() >= 200:
        screen.textinput("Game Over", "Opponent won!")
        screen.bye()

screen.listen()
screen.onkey(move_player, "space")

while True:
    move_opponent()
    check_winner()

# ------------------------------------------
# 🏓 Turtle Pong Game
# ------------------------------------------

win = turtle.Screen()
win.title("Turtle Pong")
win.bgcolor("black")
win.setup(width=600, height=400)

# Paddle
paddle = turtle.Turtle()
paddle.shape("square")
paddle.color("white")
paddle.shapesize(stretch_wid=1, stretch_len=5)
paddle.penup()
paddle.goto(0, -170)

# Ball
ball = turtle.Turtle()
ball.shape("circle")
ball.color("red")
ball.penup()
ball.speed(40)
ball.dx = 2
ball.dy = -2

# Paddle movement
def paddle_right():
    x = paddle.xcor()
    x += 20
    paddle.setx(x)

def paddle_left():
    x = paddle.xcor()
    x -= 20
    paddle.setx(x)

# Keyboard bindings
win.listen()
win.onkeypress(paddle_right, "Right")
win.onkeypress(paddle_left, "Left")

# Game loop
while True:
    win.update()

    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border collision
    if ball.xcor() > 290 or ball.xcor() < -290:
        ball.dx *= -1
    if ball.ycor() > 190:
        ball.dy *= -1

    # Paddle collision
    if (ball.ycor() < -160 and ball.ycor() > -190) and (ball.xcor() > paddle.xcor() - 50 and ball.xcor() < paddle.xcor() + 50):
        ball.dy *= -1

    # Game over
    if ball.ycor() < -190:
        win.bye()
        print("Game Over")

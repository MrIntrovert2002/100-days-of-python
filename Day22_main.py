from turtle import Turtle, Screen
from Day22_paddle import Paddle, NewPaddle
from Day22_scoreboard import Scoreboard
from Day22_ball import Ball
import time

screen = Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

def start_game():
    screen.update()
    writer = Scoreboard()
    screen.update()
    r_paddle = NewPaddle(350)
    l_paddle = NewPaddle(-350)
    b = Ball()

    screen.listen()
    screen.onkeypress(r_paddle.up, "Up")
    screen.onkeypress(r_paddle.down, "Down")
    screen.onkeypress(l_paddle.up, "a")
    screen.onkeypress(l_paddle.down, "s")

    while True:
        time.sleep(b.move_speed)
        b.move()
        screen.update()

        if r_paddle.coll(b):
            print("passle hit")
            b.setheading(180)
            b.div_change(r_paddle.passle_index)
        if l_paddle.coll(b):
            print("passle hit")
            b.setheading(0)
            b.div_change(l_paddle.passle_index)

        if b.xcor() >= 400:
            writer.l_plus()
            b.reset()
            screen.update()
            time.sleep(1)
        elif b.xcor() <= -400:
            writer.r_plus()
            b.reset()
            screen.update()
            time.sleep(1)

start_game()
screen.exitonclick()
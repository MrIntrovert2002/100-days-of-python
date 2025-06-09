from turtle import Screen
from Day20_21_snake import Snake
from Day20_21_food import Food
from Day20_21_scoreboard import Scoreboard
import time
DELAY_sec = 0.1

screen = Screen()
screen.bgcolor("black")
screen.title("Snake Game")
screen.setup(width=600, height=600)

def turn(snake):
    """Function to set up the key bindings for snake movement"""
    screen.listen()
    screen.onkey(snake.up, "Up")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.left, "Left")
    screen.onkey(snake.right, "Right")

def game_over(screen, writer, snake, f):
    """Function to handle the game over state"""
    screen.update()
    time.sleep(1)
    snake.clear_snake()
    f.hide_food()
    writer.game_over()
    screen.update()
    screen.onkey(start_game, "space")

def start_game():
    """The main Game function to start the game and reset the screen"""
    screen.clear()
    screen.tracer(0) 
    screen.bgcolor("black")

    snake = Snake()
    f = Food()
    writer = Scoreboard()
    turn(snake)

    is_game_over = False
    while is_game_over == False:
        screen.update() 
        time.sleep(DELAY_sec)
        snake.move()
        sn = snake.head

        if sn.distance(f) < 15:
            snake.add_head()
            f.refresh()
            writer.increase_score()

        if snake.self_collision():
            game_over(screen, writer, snake, f)
            is_game_over = True

        if sn.xcor() > 280 or sn.xcor() < -280 or sn.ycor() > 280 or sn.ycor() < -280:
            game_over(screen, writer, snake, f)
            is_game_over = True

start_game()
screen.exitonclick()
from turtle import Turtle, Screen
import time
import random

screen = Screen()
screen.bgcolor("black")
screen.title("Snake Game")
screen.setup(width=600, height=600)
screen.tracer(0)  # Disable automatic screen updates for smoother animation

def add_head(snake, x_pos, y_pos): # 
    """Function to add a new head to the snake"""
    new_snake = Turtle("square")
    new_snake.color("white")
    new_snake.penup()
    new_snake.speed(0)
    new_snake.shapesize(0.9, 0.9)
    x = snake[len(snake)-1].xcor() 
    y = snake[len(snake)-1].ycor() 
    new_snake.setposition(x, y)
    x_pos.append(new_snake.xcor())
    y_pos.append(new_snake.ycor())
    snake.append(new_snake)
    return snake, x_pos, y_pos

def update_snake_pos(snake, x_pos, y_pos):
    """Function to update the positions of the snake segments"""
    for i in range(len(snake)):
        x_pos[i] = snake[i].xcor()
        y_pos[i] = snake[i].ycor()
    return x_pos, y_pos

def turn_snake(sn):
    """Function to turn the snake based on key presses"""
    def head_up():
        if sn.heading() != 270:
            sn.setheading(90)
    def head_down():
        if sn.heading() != 90:
            sn.setheading(270)
    def head_left():
        if sn.heading() != 0:
            sn.setheading(180)
    def head_right():
        if sn.heading() != 180:
            sn.setheading(0)

    screen.onkey(head_up, "Up")
    screen.onkey(head_down, "Down")
    screen.onkey(head_left, "Left")
    screen.onkey(head_right, "Right")

def snake_move(snake, x_pos, y_pos):
    """Function to move the snake forward"""
    for i in range(len(snake)-1, -1, -1):
            if i == 0:
                snake[i].forward(20)
            else:
                x = x_pos[i-1]
                y = y_pos[i-1]
                snake[i].goto(x, y)

def start_game():
    """The main Game function to start the game and reset the screen"""
    screen.clear()
    screen.tracer(0) 
    screen.bgcolor("black")
    sn = Turtle()
    sn.shape("square")
    sn.color("white")
    sn.penup()
    sn.speed(0)
    sn.shapesize(0.9, 0.9)
    # sn.goto(60, 0)
    snake = []
    snake.append(sn)
    snake_xpos = [sn.xcor()]
    snake_ypos = [sn.ycor()]
    score = 0

    f = Turtle()
    f.shape("circle")
    f.shapesize(0.6, 0.6)
    f.color("blue")
    f.penup()
    f.goto(0, 40)
    f.speed(0)

    def food_t():
        """Function to randomly place the food on the screen"""
        f.hideturtle()
        x = 20*random.randint(-12, 12)
        y = 20*random.randint(-12, 12)
        f.setposition(x, y)
        f.showturtle()
        screen.update()


    screen.listen()
    turn_snake(sn)
    food_t()

    while True:
        if len(snake) < 3:
            # If the snake is too short, add a head to it
            snake, snake_xpos, snake_ypos = add_head(snake, snake_xpos, snake_ypos)
            screen.update() 
            time.sleep(0.15)
        else:
            screen.update()
            time.sleep(0.15)

        # Move the snake forward
        snake_move(snake, snake_xpos, snake_ypos)

        # Check for food collision
        if sn.distance(f) < 15:
            score += 1
            snake, snake_xpos, snake_ypos = add_head(snake, snake_xpos, snake_ypos)
            food_t()
            # print(f"Score: {score}")
            # print(f"Snake Length: {len(snake)}")

        # Check for self collision
        for i in range(2, len(snake)):
            if sn.distance(snake[i]) < 15:
                screen.textinput("Game Over", "You hit yourself! Press Enter to restart")
                start_game()

        # Check for wall collision
        if sn.xcor() > 280 or sn.xcor() < -280 or sn.ycor() > 280 or sn.ycor() < -280:
            screen.textinput("Game Over", "You hit the wall! Press Enter to restart")
            start_game()

        # Update the positions of the snake segments
        snake_xpos, snake_ypos = update_snake_pos(snake, snake_xpos, snake_ypos) 

start_game()
screen.exitonclick()
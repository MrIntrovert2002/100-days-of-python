from turtle import Turtle
TURTLE_SHAPE = "square"
TURRLE_COLOR = "white"
TURTLE_SIZE = 0.9
COLLISION_DISTANCE = 15

class Snake:
    def __init__(self):
        self.snake = []
        self.x_pos = []
        self.y_pos = []
        self.create_snake()
        self.head = self.snake[0]

    def create_snake(self):
        """Function to create the initial snake"""
        for i in range(3):
            new_snake = Turtle(TURTLE_SHAPE)
            new_snake.color(TURRLE_COLOR)
            new_snake.penup()
            new_snake.speed(0)
            new_snake.shapesize(TURTLE_SIZE, TURTLE_SIZE)
            new_snake.setposition(-20 * i, 0)
            self.snake.append(new_snake)
            self.x_pos.append(new_snake.xcor())
            self.y_pos.append(new_snake.ycor())

    def add_head(self):
        """Function to add a new head to the snake"""
        new_snake = Turtle("square")
        new_snake.color("white")
        new_snake.penup()
        new_snake.speed(0)
        new_snake.shapesize(TURTLE_SIZE, TURTLE_SIZE)
        x = self.snake[-1].xcor()
        y = self.snake[-1].ycor()
        new_snake.setposition(x, y)
        self.x_pos.append(new_snake.xcor())
        self.y_pos.append(new_snake.ycor())
        self.snake.append(new_snake)

    def update_positions(self):
        """Function to update the positions of the snake segments"""
        for i in range(len(self.snake)):
            self.x_pos[i] = self.snake[i].xcor()
            self.y_pos[i] = self.snake[i].ycor()

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)
    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)
    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)
    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)

    def move(self):
        """Function to move the snake forward"""
        for i in range(len(self.snake)-1, -1, -1):
            if i == 0:
                self.snake[i].forward(20)
            else:
                x = self.x_pos[i-1]
                y = self.y_pos[i-1]
                self.snake[i].goto(x, y)
        self.update_positions()

    def length(self):
        """Function to return the length of the snake"""
        return len(self.snake)
    
    def self_collision(self):
        """Function to check for self-collision"""
        for i in range(2, self.length()):
            if self.head.distance(self.snake[i]) < COLLISION_DISTANCE:
                return True
        return False
    
    def clear_snake(self):
        """Function to clear the snake segments"""
        for segment in self.snake:
            segment.hideturtle()
        self.snake.clear()
        self.x_pos.clear()
        self.y_pos.clear()

    # def head_pos(self):
    #     """Function to return the position of the snake head"""
    #     return self.head.xcor(), self.head.ycor()

    # def ideal_path(self):
    #     """Automatically play the snake to reach the food"""
    #     if self.head.xcor() >= 245:
    #         self.down()
    #         self.move()
    #         self.left()
    #     if self.head.xcor() <= -225 and self.head.xcor() >= -245 and self.head.ycor() <= 225 and self.head.ycor() >= -225:
    #         self.down()
    #         self.move()
    #         self.right()
    #     if self.head.xcor() <= -245:
    #         if self.head.ycor() >= 225:
    #             self.right()
    #         elif self.head.ycor() <= -225:
    #             self.up()
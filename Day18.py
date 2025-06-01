from turtle import Turtle, Screen
from random import choice
# import heroes
# import villains

timmy = Turtle()
timmy.shape("turtle")
timmy.color("red")
timmy.speed(0) # Set the speed to the fastest
timmy.pensize(2)
screen = Screen()
screen.colormode(255) # Set the color mode to 255 for RGB colors

def turn_back():
    """Turns turtle 180 degrees to the left."""
    timmy.left(180) 

def random_color():
    """Generates a random color using."""
    import random
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b

def original():
    """Turns the turtle back to its original position."""
    timmy.penup()
    timmy.goto(0, 0)
    timmy.setheading(0)
    timmy.pendown()

def go_to(x, y):
    """Moves the turtle to a specific position."""
    timmy.penup()
    timmy.goto(x, y)
    timmy.pendown()
    timmy.setheading(0)

def draw_square():
    """Draws a square with the turtle."""
    for i in range(4):
        timmy.forward(100)
        timmy.left(90)


# Draw a square
timmy.fillcolor("yellow")
timmy.begin_fill()
draw_square()
timmy.end_fill()

turn_back()
# Draw a dashed line
for i in range(10):
    timmy.forward(10)
    timmy.penup()
    timmy.forward(10)
    timmy.pendown()

go_to(-100, -100)

def draw_shape(sides):
    """Draws a shape with the given number of sides."""
    angle = 360 / sides
    for _ in range(sides):
        timmy.forward(100)
        timmy.right(angle)

# Draw shapes with 3 to 10 sides
random_color_set = ["red", "blue", "green", "yellow", "purple", "orange", "pink"] # Set of random colors
for i in range(3, 11):
    timmy.color(choice(random_color_set))  # Random color for each shape
    draw_shape(i) 

go_to(-500, 200)

# Draw a random walk with random colors 
for i in range(200):
    # timmy.color(choice(random_color_set))  # Random color for each line
    timmy.color(random_color())  # Random color for each line
    timmy.forward(30)
    timmy.setheading(choice([0, 90, 180, 270]))

def draw_spirograph(size_of_gap):
    """Draws a spirograph pattern."""
    for i in range(int(360/ size_of_gap)):
        timmy.color(random_color())  # Random color for each line
        timmy.circle(100)  # Draw a circle with radius 100
        timmy.right(size_of_gap)  # Rotate the turtle by 10 degrees

# Draw a spirograph with a gap of 10 degrees
go_to(500, 200)
draw_spirograph(10) 

screen.exitonclick()
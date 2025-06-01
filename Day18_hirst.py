import colorgram
from turtle import Turtle, Screen
from random import choice

timmy = Turtle()
timmy.speed(0) # Set the speed to the fastest
timmy.pensize(2)
screen = Screen()
screen.colormode(255) # Set the color mode to 255 for RGB colors
timmy.hideturtle()  # Hide the turtle after drawing

colors = colorgram.extract('hirst2.jpg', 30)  # Extract colors from the image
for i in range(len(colors)):
    r = colors[i].rgb.r
    g = colors[i].rgb.g
    b = colors[i].rgb.b
    colors[i] = (r, g, b)  # Convert to RGB tuple
# print(colors)  # Print the extracted colors for debugging
def go_to(x, y):
    """Moves the turtle to a specific position."""
    timmy.penup()
    timmy.goto(x, y)
    timmy.pendown()
    timmy.setheading(0)

def draw_dots(rows, cols, dot_size):
    """Draws a grid of dots."""
    timmy.penup()
    for row in range(rows):
        for col in range(cols):
            timmy.dot(dot_size, choice(colors))  # Use the extracted colors
            timmy.forward(dot_size * 2)  # Move forward by double the dot size
        timmy.backward(dot_size * 2 * cols)  # Move back to the start of the row
        timmy.right(90)  # Turn right to start a new row
        timmy.forward(dot_size * 2)  # Move down to the next row
        timmy.left(90)  # Turn left to face the original direction
    
# Draw a grid of dots
go_to(-200, 200)  # Move to the starting position
draw_dots(rows=10, cols=10, dot_size=20)
screen.exitonclick()
from turtle import Turtle, Screen
from random import choice

screen = Screen()
screen.colormode(255) # Set the color mode to 255 for RGB colors
screen.setup(width=800, height=600)

# timmy = Turtle()
# timmy.penup()
# timmy.shape("turtle")
# timmy.speed(1) # Set the speed to the fastest
# timmy.pensize(1)
# timmy.goto(-380, 200)

# def etch_a_sketch():
#     screen.title("Etch A Sketch")
#     def move_forwards():
#         """Moves the turtle forward by 10 units."""
#         timmy.forward(20)
#     def turn_left():
#         """Turns the turtle left by 5 degrees."""
#         timmy.left(10)
#     def turn_right():
#         """Turns the turtle right by 5 degrees."""
#         timmy.right(10)
#     def move_backwards():
#         """Moves the turtle backward by 10 units."""
#         timmy.backward(20)
#     def clear():
#         """Clears the screen and resets the turtle's position."""
#         timmy.clear()
#         timmy.penup()
#         timmy.goto(0, 0)
#         timmy.setheading(0)
#         timmy.pendown()

#     screen.listen()
#     screen.onkey(key="w", fun=move_forwards)
#     screen.onkey(key="a", fun=turn_left)
#     screen.onkey(key="s", fun=move_backwards)
#     screen.onkey(key="d", fun=turn_right)
#     screen.onkey(key="c", fun=clear)

# etch_a_sketch()

user_bet = screen.textinput("Make a bet", "Enter your bet (red, green, blue, yellow, purple, orange, pink, brown):")
print(user_bet)

colors = ["violet", "indigo", "blue", "green", "yellow", "orange", "red"]
def create_turtle(y_pos, no=0):
    """Creates a turtle with a random color and moves it to a random position."""
    new_turtle = Turtle()
    new_turtle.shape("turtle")
    new_turtle.color(colors[no])
    new_turtle.penup()
    new_turtle.goto(-380, y_pos)
    return new_turtle

turtles = []
for i in range(7):
    turtles.append(create_turtle(y_pos=140 - (i * 40), no=i)) # Create turtles for each color and position them
    
no_winner = False
while no_winner == False:
    for turtle in turtles:
        turtle.forward(choice(range(1, 10)))  # Move each turtle forward by a random distance
        if turtle.xcor() >= 370:  # Check if the turtle has reached the finish line
            no_winner = True
            if turtle.color()[0] == user_bet:
                screen.textinput("Winner!", f"The {turtle.color()[0]} turtle wins! You guessed right!\nPress Enter to exit.")
            else:
                screen.textinput("Loser!", f"The {turtle.color()[0]} turtle wins! You guessed wrong!\nPress Enter to exit.")
            break

screen.exitonclick()
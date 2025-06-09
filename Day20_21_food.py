from turtle import Turtle
import random
FOOD_SHAPE = "circle"
FOOD_COLOR = "blue"
FOOD_SIZE = 0.6

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape(FOOD_SHAPE)
        self.color(FOOD_COLOR)
        self.penup()
        self.speed(0)
        self.shapesize(stretch_wid=FOOD_SIZE, stretch_len=FOOD_SIZE)
        self.refresh()
    
    def refresh(self):
        """Function to randomly place the food on the screen"""
        self.hideturtle()
        x = 20 * random.randint(-12, 12)
        y = 20 * random.randint(-12, 12)
        self.goto(x, y)
        self.showturtle()
    
    def hide_food(self):
        """Function to hide the food"""
        self.hideturtle()
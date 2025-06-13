from turtle import Turtle
import random

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.speed("slowest")
        self.shapesize(0.8,0.8)
        self.color("white")
        self.penup()
        self.reset()
        
    def reset(self):
        self.hideturtle()
        self.goto(0,0)
        self.setheading(180*random.randint(0, 1)) # Start with right or left
        self.deviation_steps = random.randint(0, 5) # Incline for deviation
        self.div_dir = random.randint(0,1) # Moving direction up or down 
        self.showturtle()
        self.move_speed = 0.08

    def move(self):
        self.forward(5)
        if self.div_dir == 0:
            self.div_up(self.deviation_steps)
            if self.ycor() > 280:
                self.div_dir = 1
        elif self.div_dir == 1:
            self.div_down(self.deviation_steps)
            if self.ycor() < -280:
                self.div_dir = 0

    def div_up(self, div_steps):
        head = self.heading()
        self.setheading(90)
        self.forward(div_steps)
        self.setheading(head)

    def div_down(self, div_steps):
        head = self.heading()
        self.setheading(270)
        self.forward(div_steps)
        self.setheading(head)

    def div_change(self, index):
        self.move_speed *= 0.5
        if index == 0:
            if self.div_dir == 0:
                self.deviation_steps -=2
            else:
                self.deviation_steps +=2
            self.step_check()
        elif index == 1:
            if self.div_dir == 0:
                self.deviation_steps -=1
            else:
                self.deviation_steps +=1
            self.step_check()
        elif index == 2:
            self.step_check()
        elif index == 3:
            if self.div_dir == 0:
                self.deviation_steps +=1
            else:
                self.deviation_steps -=1
            self.step_check()
        elif index == 4:
            if self.div_dir == 0:
                self.deviation_steps +=2
            else:
                self.deviation_steps -=2
            self.step_check()

    def step_check(self):
        if self.deviation_steps < 0:
            self.deviation_steps = 0
        if self.deviation_steps > 4:
            self.deviation_steps = 4
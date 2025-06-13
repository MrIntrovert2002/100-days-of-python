from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.pencolor("white")
        self.penup()
        self.hideturtle()
        self.speed("slowest")
        self.score_r = 0
        self.score_l = 0
        self.refresh()

    def draw_line(self):
        self.goto(0, -280)
        self.setheading(90)
        self.pensize(2)
        for i in range(27):
            self.forward(10)
            self.pendown()
            self.forward(10)
            self.penup()
        self.forward(20)

    def refresh(self):
        self.clear()
        self.draw_line()
        self.backward(20)
        self.write(f"{self.score_l}      {self.score_r}", align="center", font=("Arial", 22, "normal"))

    def r_plus(self):
        self.score_r +=1
        self.refresh()

    def l_plus(self):
        self.score_l +=1
        self.refresh()
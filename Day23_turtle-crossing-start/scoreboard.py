from turtle import Turtle
FONT = ("Courier", 24, "normal")
FONT2 = ("Arial", 12, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(-280,260)
        self.level = 1
        self.refresh()

    def refresh(self):
        self.clear()
        self.write(f"Level {self.level}", False, "left", FONT)

    def increase_level(self):
        self.level+=1
        self.refresh()

    def game_over(self):
        self.clear()
        self.goto(0,20)
        self.write(f"Collision Detected.", False, "center", FONT)
        self.goto(0,-10)
        self.write(f"Game Over!", False, "center", FONT)
        self.goto(0,-30)
        self.write(f"Press Space to restart.", False, "center", FONT2)
from turtle import Turtle
SCORE_COLOR = "white"

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.color(SCORE_COLOR)
        self.goto(0, 260)
        self.update_scoreboard()

    def update_scoreboard(self):
        """Function to update the scoreboard with the current score"""
        self.clear()
        self.write(f"Score: {self.score}", align="center", font=("Arial", 14, "normal"))

    def increase_score(self):
        """Function to increase the score by 1"""
        self.score += 1
        self.update_scoreboard()
    
    def game_over(self):
        """Function to display the game over message and final score"""
        self.goto(0, 0)
        self.write("Game Over! Press Space to restart", align="center", font=("Arial", 14, "normal"))
        self.goto(0, -20)
        self.write(f"Final Score: {self.score}", align="center", font=("Arial", 14, "normal"))
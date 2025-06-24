from turtle import Turtle
SCORE_COLOR = "white"

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.highscore = self.read_hs()
        self.hideturtle()
        self.penup()
        self.color(SCORE_COLOR)
        self.goto(0, 260)
        self.update_scoreboard()

    def read_hs(self):
        with open("Day24_snake_highscore.txt") as f:
            hs = int(f.read())
        return hs

    def update_scoreboard(self):
        """Function to update the scoreboard with the current score"""
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.highscore}", align="center", font=("Arial", 14, "normal"))

    def increase_score(self):
        """Function to increase the score by 1"""
        self.score += 1
        self.update_scoreboard()

    def game_over(self):
        """Function to display the game over message and final score"""
        self.clear()
        self.goto(0, 0)
        self.write("Game Over! Press Space to restart", align="center", font=("Arial", 14, "normal"))
        self.goto(0, -20)
        self.write(f"Final Score: {self.score}", align="center", font=("Arial", 14, "normal"))
        h_score_str = f"High Score: {self.highscore}"
        if self.score > self.highscore:
            self.highscore = self.score
            h_score_str = f"New High Score: {self.highscore}"
            with open("Day24_snake_highscore.txt", "w") as f:
                f.write(f"{self.highscore}")
        self.score = 0
        self.goto(0, -40)
        self.write(h_score_str, align="center", font=("Arial", 14, "normal"))
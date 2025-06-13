from turtle import Turtle

class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.speed("slowest")
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.setheading(90)

    def up(self):
        self.forward(20)
    def down(self):
        self.backward(20)

class NewPaddle():
    def __init__(self, pos):
        self.paddle_list = []
        self.create_passle(pos)

    def create_passle(self, pos):
        for i in range(-2, 3):
            new_paddle = Turtle()
            new_paddle.shape("square")
            new_paddle.color("white")
            new_paddle.penup()
            new_paddle.speed("slowest")
            new_paddle.goto(pos,20*i)
            self.paddle_list.append(new_paddle)

    def up(self):
        for i in self.paddle_list:
            new_y = i.ycor()+20
            i.goto(i.xcor(), new_y)

    def down(self):
        for i in self.paddle_list:
            new_y = i.ycor()-20
            i.goto(i.xcor(), new_y)

    def coll(self, ball):
        for i in range(len(self.paddle_list)):
            if self.paddle_list[i].distance(ball)<15:
                print(i)
                self.passle_index = i
                return True
        return False
from turtle import Turtle

class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.penup()
        self.goto(position)

    def go_up():
        new_y = self.ycor() + 20
        self.paddle.goto(self.paddle.xcor(), new_y)


    def go_down():
        new_y = paddle.ycor() - 20
        paddle.goto(paddle.xcor(), new_y)
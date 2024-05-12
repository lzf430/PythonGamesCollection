from turtle import Turtle, Screen
from paddle import Paddle

# screen setup
screen = Screen()
screen.setup(width=800, height=600)
screen.title("Pong Game")
screen.bgcolor("black")
screen.tracer(0)

right_paddle = Paddle((-350, 0))



screen.listen()
screen.onkeypress(paddle.go_up, "Up")
screen.onkeypress(paddle.go_down, "Down")

game_is_on = True
while game_is_on:
    screen.update()

































screen.exitonclick()



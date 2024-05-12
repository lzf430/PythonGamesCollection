from turtle import Turtle
import random

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)    # initially is 20x20 pixel, times 0.5 to make it 10x10 pixel
        self.color("red")
        self.speed(0)
        self.refresh_food()

    def refresh_food(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)


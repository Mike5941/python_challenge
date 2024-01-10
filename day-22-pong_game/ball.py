from turtle import Turtle, Screen
import math


# SCREEN_SIZE = Screen().screensize()
# X = SCREEN_SIZE[0]
# Y = SCREEN_SIZE[1]
# radian = math.atan2(__y=Y, __x=X)
# degree = math.degrees(radian)


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1
        # self.setheading(degree)

    def move(self):
        # self.forward(10)
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1
        self.move_speed *= 0.9

    def bounce_x(self):
        self.x_move *= -1

    def reset_position(self):
        self.goto(0, 0)
        self.move_speed = 0.1
        self.bounce_x()



import random
from random import choice, randint
from turtle import Turtle, Screen
import turtle as t


tim = Turtle()
t.colormode(255)

tim.speed("fastest")
tim.pensize(10)


def random_direction():
    angle = [0, 90, 180, 270]
    tim.left(choice(angle))


def random_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    random_color = (r, g, b)
    return random_color


for _ in range(100):
    tim.pen(fillcolor=random_color(), pencolor=random_color())
    tim.forward(30)
    random_direction()

screen = Screen()
screen.exitonclick()

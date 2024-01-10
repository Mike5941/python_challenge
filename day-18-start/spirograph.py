import turtle as t
from random import randint


def random_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    rgb = (r, g, b)
    return rgb


t.colormode(255)
tim = t.Turtle()
t.speed("fastest")


for x in range(0, 361, 5):
    t.circle(50)
    t.color(random_color())
    t.tiltangle(x)
    t.setheading(x)

screen = t.Screen()
screen.exitonclick()

from turtle import Turtle, Screen
from colors import color
from random import choice

tim = Turtle()
rgb = color.keys()


def draw(num_of_sides):
    for _ in range(num_of_sides):
        tim.forward(100)
        tim.right(360 / num_of_sides)


def import_random_color():
    tim.color(choice(list(rgb)))


for nums_of_sides in range(3, 11):
    import_random_color()
    draw(nums_of_sides)








screen = Screen()
screen.exitonclick()
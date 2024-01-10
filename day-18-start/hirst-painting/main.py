# import colorgram
#
# colors = colorgram.extract('image.jpg', 35)
#
#
# rgb = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     rgb.append((r, g, b))
#
# print(rgb)


import turtle as t
from turtle import Turtle, Screen
from random import choice

# dotsize = 20
# width x height = 100
# dot_per_space = 50


color_list = [
    (54, 108, 149), (225, 201, 108), (134, 85, 58), (229, 235, 234), (224, 141, 62), (197, 144, 171),
    (143, 180, 206), (137, 82, 106), (210, 90, 68), (232, 226, 194), (188, 78, 122), (69, 101, 86),
    (132, 183, 132), (65, 156, 86), (137, 132, 74), (48, 155, 195), (183, 191, 202), (232, 221, 225), (58, 47, 41),
    (47, 59, 96), (38, 44, 64), (106, 46, 54), (41, 55, 48), (12, 104, 95), (118, 125, 145), (182, 194, 199),
    (215, 176, 187), (223, 178, 168), (54, 45, 52), (179, 199, 184), (133, 41, 39), (76, 63, 49), (38, 79, 82)
]

t.colormode(255)
tim = Turtle()

x = -225
y = -225

tim.penup()
tim.hideturtle()
tim.setpos(x, y)
tim.speed("fastest")

for _ in range(1, 101):
    tim.dot(20, choice(color_list))
    tim.forward(50)
    if _ % 10 == 0:
        y += 50
        tim.setpos(x, y)









screen = Screen()
screen.exitonclick()
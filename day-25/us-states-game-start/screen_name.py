from turtle import Turtle


class State(Turtle):

    def __init__(self, state_name, position):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(position)
        self.write(state_name, align="center")

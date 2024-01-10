import turtle
import pandas
from screen_name import State

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)


data = pandas.read_csv("50_states.csv")

game_is_running = True
guessed_states = []
all_states = data.state.array
while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct",
                                    prompt="What's another state's name?").title()

    if answer_state == "Exit":
        new_data = pandas.DataFrame(list(set(all_states) - set(guessed_states)))
        new_data.to_csv("states_to_learn.csv")
        break

    if answer_state in all_states:
        guessed_states.append(answer_state)
        state_info = data[data.state == answer_state]
        state_name = state_info.state.item()
        state_position = (int(state_info.x), int(state_info.y))
        display_state = State(state_name, state_position)


from tkinter import *
from tkinter import messagebox
from random import choice
import os
import pandas



BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}

try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")

def next_card():
    global current_card, flip_timer
    try:
        current_card = choice(to_learn)
    except IndexError:
        os.remove("data/words_to_learn.csv")
        messagebox.showinfo(title="Complete!", message="Well, done!")
        exit()
    window.after_cancel(flip_timer)
    french_word = current_card.get('French')
    canvas.itemconfig(front_card, image=card_front_img)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_text, text=f"{french_word}", fill="black")
    flip_timer = window.after(3000, flip_card)

def filtering_correction():
    next_card()
    to_learn.remove(current_card)
    df = pandas.DataFrame(to_learn)
    df.to_csv("data/words_to_learn.csv", index=False)


def flip_card():
    english_word = current_card.get('English')
    canvas.itemconfig(front_card, image=card_back_img)
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_text, text=f"{english_word}", fill="white")


window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, flip_card)


canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, hi2ghlightthickness=0)
card_front_img = PhotoImage(file="./images/card_front.png", )
card_back_img = PhotoImage(file="./images/card_back.png")
front_card = canvas.create_image(400, 263, image=card_front_img)
card_title = canvas.create_text(400, 150, text="French", font=("Ariel", 40, "italic"), fill="black")
card_text = canvas.create_text(400, 263, text="trouve", font=("Ariel", 60, "bold"), fill="black")
canvas.grid(row=0, column=0, columnspan=2)

right_img = PhotoImage(file="./images/right.png")
right_btn = Button(image=right_img, highlightbackground=BACKGROUND_COLOR, highlightthickness=0,
                   command=filtering_correction)
right_btn.grid(row=1, column=1)

wrong_img = PhotoImage(file="./images/wrong.png")
wrong_btn = Button(image=wrong_img, highlightbackground=BACKGROUND_COLOR, highlightthickness=0, command=next_card)
wrong_btn.grid(row=1, column=0)

next_card()

window.mainloop()
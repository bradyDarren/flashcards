from tkinter import *
import random as r 
import pandas as pd

BACKGROUND_COLOR = "#B1DDC6"
# ------------------ Random Word Generation ---------------------------------
spanish = pd.read_csv(filepath_or_buffer='data/spanish.csv')
data_dict = spanish.to_dict(orient='records')

def new_word():
    rand_word = r.choice(data_dict)['Spanish Word']
    canvas.itemconfig(word, text=rand_word)

# ---------------------------- UI -------------------------------------------
window = Tk() 
window.title("Spanish Flashcards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# -------------------------- Canvas ------------------------------------------
beg_word = r.choice(data_dict)['Spanish Word']
canvas = Canvas(width=800, height=526, highlightthickness=0,bg=BACKGROUND_COLOR)
card_pos = PhotoImage(file='images/card_front.png')
canvas.create_image(400,263,image = card_pos)
title = canvas.create_text(400, 150,text='Spanish', font=('Ariel', 40,'italic'), fill='black')
word = canvas.create_text(400, 263, text=beg_word, font=('Ariel', 60,'bold'), fill='black')
canvas.grid(column=0, row=0, columnspan=2)

# -------------------------- Buttons ------------------------------------------
unkown_image = PhotoImage(file="images/wrong.png")
unkown_button = Button(image=unkown_image, borderwidth=0, relief='flat', highlightthickness=0, command=new_word)
unkown_button.grid(column=0, row=1)

known_image = PhotoImage(file="images/right.png")
known_button = Button(image=known_image, borderwidth=0, relief='flat', highlightthickness=0, command=new_word)
known_button.grid(column=1, row=1)


window.mainloop()
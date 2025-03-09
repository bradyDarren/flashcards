from tkinter import *
import random as r 
import pandas as pd

BACKGROUND_COLOR = "#B1DDC6"
# ------------------ Random Word Generation ---------------------------------
spanish = pd.read_csv(filepath_or_buffer='data/spanish.csv')
to_learn = spanish.to_dict(orient='records')

def new_word():
    new_card = r.choice(to_learn)['Spanish Word']
    canvas.itemconfig(card_word, text=new_card)
    canvas.itemconfig(card_title, text= "Spanish")

# ---------------------------- UI -------------------------------------------
window = Tk() 
window.title("Spanish Flashcards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# -------------------------- Canvas ------------------------------------------
canvas = Canvas(width=800, height=526, highlightthickness=0,bg=BACKGROUND_COLOR)
card_pos = PhotoImage(file='images/card_front.png')
canvas.create_image(400,263,image = card_pos)
card_title = canvas.create_text(400, 150,text='', font=('Ariel', 40,'italic'), fill='black')
card_word = canvas.create_text(400, 263, text='', font=('Ariel', 60,'bold'), fill='black')
canvas.grid(column=0, row=0, columnspan=2)

# -------------------------- Buttons ------------------------------------------
unkown_image = PhotoImage(file="images/wrong.png")
unkown_button = Button(image=unkown_image, borderwidth=0, relief='flat', highlightthickness=0, command=new_word)
unkown_button.grid(column=0, row=1)

known_image = PhotoImage(file="images/right.png")
known_button = Button(image=known_image, borderwidth=0, relief='flat', highlightthickness=0, command=new_word)
known_button.grid(column=1, row=1)

new_word()

window.mainloop()
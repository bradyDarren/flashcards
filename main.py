from tkinter import *
import random as r 
import pandas as pd

BACKGROUND_COLOR = "#B1DDC6"
# ------------------ Random Word Generation ---------------------------------
try:
    spanish = pd.read_csv(filepath_or_buffer="words_to_learn.csv")
except FileNotFoundError:         
    spanish = pd.read_csv(filepath_or_buffer='data/spanish.csv')
finally:
    to_learn = spanish.to_dict(orient='records')
    current_card = {}


def new_word():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = r.choice(to_learn)
    canvas.itemconfig(card_word, text=current_card['Spanish Word'], fill = 'black')
    canvas.itemconfig(card_title, text= "Spanish", fill='black')
    canvas.itemconfig(background, image = card_front)
    window.after(3000, func=flip_card)

unkown_words = []

def words_to_study():
    unkown_words.append(current_card)
    df = pd.DataFrame(unkown_words) 
    df.to_csv("words_to_learn.csv",index=False )
    new_word()

# ---------------------------- Card Flip -------------------------------------------

def flip_card():
    canvas.itemconfig(background, image = card_back)
    canvas.itemconfig(card_title, text = 'English', fill = 'white')
    canvas.itemconfig(card_word, text = current_card['English Translation'], fill = 'white')

# ---------------------------- UI -------------------------------------------
window = Tk() 
window.title("Spanish Flashcards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

# -------------------------- Canvas ------------------------------------------
canvas = Canvas(width=800, height=526, highlightthickness=0,bg=BACKGROUND_COLOR)
card_front = PhotoImage(file='images/card_front.png')
card_back = PhotoImage(file='images/card_back.png')

background = canvas.create_image(400,263,image = card_front)
card_title = canvas.create_text(400, 150,text='', font=('Ariel', 40,'italic'), fill='black')
card_word = canvas.create_text(400, 263, text='', font=('Ariel', 60,'bold'), fill='black')
canvas.grid(column=0, row=0, columnspan=2)

# -------------------------- Buttons ------------------------------------------
unkown_image = PhotoImage(file="images/wrong.png")
unkown_button = Button(image=unkown_image, borderwidth=0, relief='flat', highlightthickness=0, command=words_to_study)
unkown_button.grid(column=0, row=1)

known_image = PhotoImage(file="images/right.png")
known_button = Button(image=known_image, borderwidth=0, relief='flat', highlightthickness=0, command=new_word)
known_button.grid(column=1, row=1)

new_word()

window.mainloop()
from tkinter import * 

BACKGROUND_COLOR = "#B1DDC6"
# ------------------------------------- UI --------------------------------
window = Tk() 
window.title("Spanish Flashcards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# Canvas
canvas = Canvas(width=800, height=526, highlightthickness=0,bg=BACKGROUND_COLOR)
card_pos = PhotoImage(file='images/card_front.png')
canvas.create_image(400,263,image = card_pos)
canvas.grid(column=0, row=0, columnspan=2)
 
#Labels
language = Label(text='Title', font=('Ariel', 40,'italic'), bg='white',fg='black')
language.place(x=310,y=150)
word = Label(text='word', font=('Ariel', 60, 'bold'), fg='black', bg='white')
word.place(x=290, y=263)

# Buttons
wrong_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_image, borderwidth=0, relief='flat', highlightthickness=0)
wrong_button.grid(column=0, row=1)
right_image = PhotoImage(file="images/right.png")
right_button = Button(image=right_image, borderwidth=0, relief='flat', highlightthickness=0)
right_button.grid(column=1, row=1)



window.mainloop()
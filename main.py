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
canvas.create_text(400, 150,text='Title', font=('Ariel', 40,'italic'), fill='black')
canvas.create_text(400, 263, text='word', font=('Ariel', 60,'bold'), fill='black')
canvas.grid(column=0, row=0, columnspan=2)

# Buttons
unkown_image = PhotoImage(file="images/wrong.png")
unkown_button = Button(image=unkown_image, borderwidth=0, relief='flat', highlightthickness=0)
unkown_button.grid(column=0, row=1)
known_image = PhotoImage(file="images/right.png")
known_button = Button(image=known_image, borderwidth=0, relief='flat', highlightthickness=0)
known_button.grid(column=1, row=1)



window.mainloop()
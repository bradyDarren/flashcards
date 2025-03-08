from tkinter import * 

BACKGROUND_COLOR = "#B1DDC6"
# ------------------------------------- UI --------------------------------
window = Tk() 
window.title("Spanish Flashcards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# canvas
canvas = Canvas(width=800, height=526, highlightthickness=0)
card_pos = PhotoImage(file='card_front.png')
canvas.create_image(400,263,image = card_pos)
canvas.grid(column=0, row=0, columnspan=2)
canvas.config(bg=BACKGROUND_COLOR)

# buttons
wrong_image = PhotoImage(file="wrong.png")
wrong_button = Button(image=wrong_image, borderwidth=0, relief='flat', highlightthickness=0)
wrong_button.grid(column=0, row=1)
right_image = PhotoImage(file="right.png")
right_button = Button(image=right_image, borderwidth=0, relief='flat', highlightthickness=0)
right_button.grid(column=1, row=1)


window.mainloop()
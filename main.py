from tkinter import * 

BACKGROUND_COLOR = "#B1DDC6"

# ------------------------------------- UI --------------------------------
window = Tk() 
window.title("Spanish Flashcards")
window.config(padx=50, pady=50)

canvas = Canvas(width=800, height=526, highlightthickness=0)
card_pos = PhotoImage(file='card_front.png')
canvas.create_image(400,263,image = card_pos)
canvas.grid(column=0, row=0)


window.mainloop()
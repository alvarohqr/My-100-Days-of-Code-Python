from tkinter import *
import pandas as pd
from random import choice, randint
WIDTH = 800
HEIGHT = 526
BACKGROUND_COLOR = "#B1DDC6"

#----------------------------------NEXT CARD----------------------------------
def next_card():
    try:
        data = pd.read_csv("Day 31/data/french_words.csv")
    except TypeError:
        print("Not such file found.")
    else:
        to_learn = data.to_dict(orient="records")  
        french_word =  choice(to_learn)["French"]
        print(french_word) 
        canvas.itemconfig(card_title, text="French")
        canvas.itemconfig(card_word, text= french_word)
        # french_word = data.to_dict()
        # index = randint(0,100)
        # french_word = french_word["French"][index] 
        # canvas.create_text(400,150,text=french_word, font=("Ariel", 40, "italic"))
        

#----------------------------------UI SETUP----------------------------------
window = Tk()
window.title("Flash Card App") 
window.config(padx=50, pady=50, background=BACKGROUND_COLOR)

#Front Flash Card
canvas = Canvas(width=WIDTH, height=HEIGHT, highlightthickness=0, background=BACKGROUND_COLOR)
card_front = PhotoImage(file="Day 31/images/card_front.png")
canvas.create_image(WIDTH/2, HEIGHT/2,image=card_front)
card_title = canvas.create_text(400,150,text="", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(WIDTH/2, HEIGHT/2,text="", font=("Ariel", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

#Back Flash Card
# back = Canvas()
# card_back = PhotoImage(file="Day 31/images/card_back.png")
# back.create_image(800,526,image=card_back)
# back.grid(column=0, row=0, columnspan=2)

#Buttons
wrong = PhotoImage(file="Day 31/images/wrong.png")
wrong_button = Button(image=wrong, background=BACKGROUND_COLOR, highlightthickness=0, command=next_card) 
wrong_button.grid(column=0, row=1)

right = PhotoImage(file="Day 31/images/right.png")
right_button = Button(image=right, background=BACKGROUND_COLOR, highlightthickness=0, command=next_card) 
right_button.grid(column=1, row=1)

next_card()

window.mainloop()

from tkinter import *
import pandas as pd
from random import choice, randint
WIDTH = 800
HEIGHT = 526
BACKGROUND_COLOR = "#B1DDC6"
current_card = {} 
to_learn = {}
try:
    data = pd.read_csv("Day 31/data/words_to_learn.csv.csv")
except FileNotFoundError:
    original_data = pd.read_csv("Day 31/data/french_words.csv")
    to_learn = original_data.to_dict(orient="records") 
else:       
    to_learn = data.to_dict(orient="records")  
    
#----------------------------------NEXT CARD----------------------------------
def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card =  choice(to_learn)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text= current_card["French"], fill="black") 
    canvas.itemconfig(card_background, image=card_front) 
    flip_timer = window.after(3000, func=flip_card)

#----------------------------------FLIP CARD----------------------------------    
def flip_card(): 
    canvas.itemconfig(card_title, text="Enlgish", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_background, image=card_back) 

#----------------------------------REMOVE CARD----------------------------------
def is_known():
    to_learn.remove(current_card)
    data = pd.DataFrame(to_learn)
    data.to_csv("Day 31/data/words_to_learn.csv", index=False)
    next_card()


#----------------------------------UI SETUP----------------------------------
window = Tk()
window.title("Flash Card App") 
window.config(padx=50, pady=50, background=BACKGROUND_COLOR)
flip_timer = window.after(3000, func=flip_card)

#Front Flash Card
canvas = Canvas(width=WIDTH, height=HEIGHT, highlightthickness=0, background=BACKGROUND_COLOR)
card_front = PhotoImage(file="Day 31/images/card_front.png")
card_back = PhotoImage(file="Day 31/images/card_back.png")
card_background = canvas.create_image(WIDTH/2, HEIGHT/2,image=card_front) 
card_title = canvas.create_text(400,150,text="", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(WIDTH/2, HEIGHT/2,text="", font=("Ariel", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

#Buttons
wrong = PhotoImage(file="Day 31/images/wrong.png")
wrong_button = Button(image=wrong, background=BACKGROUND_COLOR, highlightthickness=0, command=next_card) 
wrong_button.grid(column=0, row=1)

right = PhotoImage(file="Day 31/images/right.png")
right_button = Button(image=right, background=BACKGROUND_COLOR, highlightthickness=0, command=is_known) 
right_button.grid(column=1, row=1)

next_card()

window.mainloop()
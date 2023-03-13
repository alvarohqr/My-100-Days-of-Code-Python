from tkinter import *

def button_clicked(): 
    my_label.config(text=input.get())

window = Tk()
window.title("Tkinter GUI")
window.minsize(480, 480)

#Label
my_label = Label(text="I'am a label", font=("Arial", 26, "bold"))
my_label["text"] = "New Text"
my_label.config(text="New Text 2")
my_label.pack(side="left")

#Button
button = Button(text="Click me", command=button_clicked)
button.pack(side="left")

#Entry
input = Entry(width=10)
input.pack(side="left")

window.mainloop()
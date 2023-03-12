from tkinter import *

window = Tk()
window.title("Tkinter GUI")
window.minsize(480, 480)

#Label
my_label = Label(text="I'am a label", font=("Arial", 26, "bold"), height=4)
my_label.pack()

my_label["text"] = "New Text"
my_label.config(text="New Text 2")

button = Button(text="Click me")
button.pack()

window.mainloop()
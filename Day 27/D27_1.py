from tkinter import *

window = Tk()
window.title("Tkinter GUI")
window.minsize(480, 480)

#Label
my_label = Label(text="I'am a label", font=("Arial", 26, "bold"), height=4)
my_label.pack()

my_label["text"] = "New Text"
my_label.config(text="New Text 2")

#Button
def button_clicked():
    global my_label
    my_label.config(text="Button got clicked")

button = Button(text="Click me", command=button_clicked)
button.pack()

window.mainloop()
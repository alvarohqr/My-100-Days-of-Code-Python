from tkinter import *

def button_clicked(): 
    my_label.config(text=input.get())

window = Tk()
window.title("Tkinter GUI")
window.minsize(480, 480)
#Add more space around the window edges
window.config(padx=200, pady=200)

#Label
my_label = Label(text="I'am a label", font=("Arial", 12, "bold"))
my_label["text"] = "New Text"
my_label.config(text="New Text 2", padx=50, pady=50)

# my_label.pack(side="left")
#my_label.place(x=100,y=200)
my_label.grid(column=0, row=0)


#Button
button = Button(text="Click me", command=button_clicked)
# button.pack(side="left")
button.grid(column=1,row=1)
button2 = Button(text="New Button")
button2.grid(column=2,row=0)

#Entry
input = Entry(width=10)
# input.pack(side="left")
input.grid(column=3,row=3)

window.mainloop()
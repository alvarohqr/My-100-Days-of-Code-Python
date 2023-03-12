import tkinter

window = tkinter.Tk()
window.title("Tkinter GUI")
window.minsize(480, 480)

#Label
my_label = tkinter.Label(text="I'am a label", font=("Arial", 26, "bold"), height=4)
my_label.pack(side="left")

my_label["text"] = "New Text"
my_label.config(text="New Text 2")

window.mainloop()
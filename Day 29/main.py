from tkinter import *
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
#Window setup
window = Tk()
window.config(padx=20, pady=20)
window.title("Password manager")

#Canvas setup
canvas = Canvas(width=200, height=200, highlightthickness=0)
my_pass_img = PhotoImage(file="Day 29/logo.png")
canvas.create_image(100, 100, image=my_pass_img)
canvas.grid(column=1, row=1)

window.mainloop()
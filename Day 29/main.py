from tkinter import *
FONT_NAME = "Arial"
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
#Window setup
window = Tk()
window.config(padx=50, pady=50)
window.title("Password manager")

#Canvas setup
canvas = Canvas(width=200, height=200, highlightthickness=0)
my_pass_img = PhotoImage(file="Day 29/logo.png")
canvas.create_image(100, 100, image=my_pass_img)
canvas.grid(column=1, row=0)
 
#LABELS
web_label = Label(text="Website:")
web_label.grid(column=0, row=1)
email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)
password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

#ENTRIES
web_entry = Entry(width=56)
web_entry.grid(column=1, row=1, columnspan=2) 
email_entry = Entry(width=56)
email_entry.grid(column=1, row=2, columnspan=2)
password_entry = Entry(width=38)
password_entry.grid(column=1, row=3)

#BUTTONS
password_button = Button(text="Generate Password")
password_button.grid(column=2, row=3) 
add_button = Button(text="Add", width=48)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
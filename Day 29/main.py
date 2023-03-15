from tkinter import * 
FONT_NAME = "Arial"
import string
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

characters = [char for char in string.printable]
print(characters)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_password():
    password = password_entry.get()
    website = web_entry.get()
    email = email_entry.get()
    with open("Day 29/data.txt", mode="a") as data:
        data.write(f"{website}\t | \t{email}\t | \t{password}\n")
    web_entry.delete(0, END)
    password_entry.delete(0, END)

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
web_entry.focus()
email_entry = Entry(width=56)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(0, "alvaro@gmail.com")
password_entry = Entry(width=38)
password_entry.grid(column=1, row=3)

#BUTTONS
password_button = Button(text="Generate Password")
password_button.grid(column=2, row=3) 
add_button = Button(text="Add", width=48, command=save_password)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
from tkinter import * 
from tkinter import messagebox
import string
from random import choice, randint, shuffle
import pyperclip

FONT_NAME = "Arial"
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
   
def generate_password():
    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [str(choice(numbers)) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    pyperclip.copy(password)
    password_entry.insert(0, password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_password():
    password = password_entry.get()
    website = web_entry.get()
    email = email_entry.get()
    
    #Alert popup window
    if not(len(password)) or not(len(website)):
        messagebox.showwarning(title="ERROR", message="Empty Website or Password!")
    else:
        #Confirmation popup window
        is_ok = messagebox.askokcancel(title=website, message=f"This are the details entered:\nEmail: {email}\nPaswword{password}\nIs it ok to save?")
        
        if is_ok:
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
password_button = Button(text="Generate Password", command=generate_password)
password_button.grid(column=2, row=3) 
add_button = Button(text="Add", width=48, command=save_password)
add_button.grid(column=1, row=4, columnspan=2) 
window.mainloop()
from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
CHECK_MARK = "✔"

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    count_down(5 * 60) 
    

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_min = int(count / 60) 
    
    count_seg = count % 60
    if count_seg < 10:
        count_seg = "0" + str(count_seg) 
        #count_seg = f"0{count_seg}" instructor solution
    
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_seg}")
    if count > 0:
        window.after(1000, count_down, count - 1)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, background=YELLOW)

# def say_something(a, b, c):
#     print(a, b, c)

# window.after(1000, say_something, 1, 10, 100)


canvas = Canvas(width=200, height=224, background=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="Day 28/tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 135, text="00:00", font=(FONT_NAME, 35, "bold"), fill="white")
canvas.grid(column=1, row=1) 

timer_label = Label(text="Timer", font=(FONT_NAME, 42, "bold"), background=YELLOW, fg=GREEN)
timer_label.grid(column=1, row=0)

#Start and reset buttons
start_button = Button(text="Start", font=(FONT_NAME, 10, "bold"), command=start_timer, highlightthickness=0)
start_button.grid(column=0, row=2)
reset_button = Button(text="Reset", font=(FONT_NAME, 10, "bold"), highlightthickness=0)
reset_button.grid(column=2, row=2)

#Check label
check_label = Label(text=CHECK_MARK, background=YELLOW, fg=GREEN)
check_label.grid(column=1, row=3)

window.mainloop()
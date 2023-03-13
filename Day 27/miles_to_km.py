from tkinter import *

MILE_TO_KM= 1.609

def miles_to_km():
    '''Display te miles in km'''
    _miles = float(miles.get())
    _km = _miles * MILE_TO_KM
    converted_label.config(text=round(_km,2))

#400 x 250 pixel window 
window = Tk()
window.title("Miles to Km Converter")
window.minsize(300, 120)
window.config(padx=20, pady=20)

#Static labels
label = Label(text="is equal to", font=("Arial", 12, "bold"))
label.grid(column=0, row=1)
label.config(padx=10)

miles_label = Label(text="Miles", font=("Arial", 12, "bold"))
miles_label.grid(column=2, row=0)
miles_label.config(padx=10)

km_lablel = Label(text="Km", font=("Arial", 12, "bold"))
km_lablel.config(padx=10)
km_lablel.grid(column=2, row=1)

#Miles entry box
miles = Entry(width=10)
miles.grid(column=1, row=0)

#Dinamic convert label
converted_label = Label(text="0", font=("Arial", 12, "bold"))
converted_label.grid(column=1,row=1)

#Calculate button
convert_button = Button(text="Calculate", font=("Arial", 12, "bold"),command=miles_to_km)
convert_button.grid(column=1, row=2)

window.mainloop()
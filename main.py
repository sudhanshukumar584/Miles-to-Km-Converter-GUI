from tkinter import *


def miles_to_km():
    miles = float(input_miles.get())
    km = miles * 1.609
    km_result_label.config(text=f"{km}")


window = Tk()
window.title("Mile to Km Converter")
window.config(padx=20, pady=20)

input_miles = Entry(width=10)
input_miles.grid(column=1, row=0)

my_label = Label(text="Miles")
my_label.grid(column=2, row=0)

is_equal_label = Label(text="is equal to")
is_equal_label.grid(column=0, row=1)

km_result_label = Label(text="0")
km_result_label.grid(column=1, row=1)

km_label = Label(text="Km")
km_label.grid(column=2, row=1)

button = Button(text="Calculate", command=miles_to_km)
button.grid(column=1, row=2)

window.mainloop()

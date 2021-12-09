from tkinter import *

window = Tk()

window.title("Convet Miles to KM in using this simple user intrface")
window.minsize(width=300, height=150)


my_label = Label(text="Miles to KM converter", font=("Arial", 21, "bold"))
my_label.grid(column=0, row=0, padx=100)

number1 = Label(text="Distance in miles", font=("Arial", 10, "bold"))
number1.grid(column=0, row=1)
first_number = Entry(width=10)
first_number.grid(column=0, row=2)


def miles_to_km():
	result = int(first_number.get()) * 1.609
	addition_result = Label(text=f"Distance in KM: {result}", font=("Arial", 15, "normal"))
	addition_result.grid(column=0, row=4)


button = Button(text="Calculate", command=miles_to_km)
button.grid(column=0, row=3)




window.mainloop()



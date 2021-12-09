from tkinter import *

window = Tk()

window.title("This is first GUI application")
window.minsize(width=600, height=400)


my_label = Label(text="Add two Numbers", font=("Arial", 21, "bold"))
# my_label.pack()
# my_label.place(x=300, y=200)
# my_label.grid(column=0, row=0)

sum = 0

number1 = Label(text="Give first number", font=("Arial", 10, "bold"))
number1.pack()
first_number = Entry(width=10)
first_number.pack()

number2 = Label(text="Give second number", font=("Arial", 10, "bold"))
number2.pack()
second_number= Entry(width=10)
second_number.pack()


def add_two_numbers():
	global sum
	sum = int(first_number.get()) + int(second_number.get())
	addition_result = Label(text=f"Sum: {sum}", font=("Arial", 20, "normal"))

	addition_result.pack()



button = Button(text="Get Sum", command=add_two_numbers)
button.pack()




window.mainloop()



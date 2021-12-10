
# TODO: Used different logic in some part, still small fix need to done
from tkinter import *
import time
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 1
LONG_BREAK_MIN = 1
reset_all = False
reps = 0
tick_mark_position = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_all():
	global timer

	window.after_cancel(timer)
	main_title["text"] = "Timer"
	canvas.itemconfig(show_timer, text="00:00")
	tick_mark.config(text="")
	global reps
	reps = 0
# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():

	global reps
	global tick_mark_position
	reps += 1

	work_sec = WORK_MIN * 60
	short_breaak_sec = SHORT_BREAK_MIN * 60
	long_break_Sec = LONG_BREAK_MIN * 60

	if reps & 1:
		main_title.config(text="Focus", fg=GREEN)
		count_down(work_sec)

	if reps % 2 == 0:
		tick_mark.config(text="✔")
		tick_mark.grid(column=1, row=(3 + tick_mark_position))
		tick_mark_position += 1
		main_title.config(text="Break", fg=PINK)
		count_down(short_breaak_sec)

	if reps % 8 == 0:
		main_title.config(text="Break", fg=RED)
		count_down(long_break_Sec)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(count):
	
	minutes = count // 60
	seconds = (count % 60)

	# for showing timer in 00:00 in this format
	if seconds < 10:
		seconds = f"0{seconds}"

		
	# for showing timer in 00:00 in this format
	if minutes <=9:
		extra_zero_for_min = "0"
	else:
		extra_zero_for_min = ""

	canvas.itemconfig(show_timer, text=f"{extra_zero_for_min}{minutes}:{seconds}")
	if count > 0:
		global timer 
		timer = window.after(1000, count_down, count - 1)
	else:
		start_timer()
	

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()

window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

main_title = Label(text="Timer",fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50, "normal"))
main_title.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, bg=YELLOW)
tomato_image = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_image)
show_timer = canvas.create_text(103, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

tick_mark = Label(text="--", fg=GREEN, font=("Arial", 20, "normal"))
tick_mark.grid(column=1, row=3)



start_button = Button(text="Start", fg=RED, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", fg=RED, command=reset_all)
reset_button.grid(column=2, row=2)


window.mainloop()
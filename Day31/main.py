from tkinter import *
from tkinter import messagebox
import random
import pandas

BACKGROUND_COLOR = "#B1DDC6"

random_english_word = ""
random_french_word = ""
random_word_idx = 0

# TODO: need to review card flipping logic
# TODO: design scoreboard functionality
#---------------- some processing ---------------

data = pandas.read_csv("data/french_words.csv")

french_words = []
for word in data["French"]:
	french_words.append(word)

english_words = []
for word in data["English"]:
	english_words.append(word)

word_dict = {
	"English": english_words,
	"French": french_words 
}

def give_random_idx():
	random_word_idx = random.randint(0, len(english_words) - 1)
	return random_word_idx


def random_words():
	global random_word_idx
	random_word_idx = give_random_idx()
	global random_french_word 
	global random_english_word 
	# print("idx", random_word_idx)
	try:
		random_french_word = word_dict["French"][random_word_idx]
		random_english_word = word_dict["English"][random_word_idx]
	except IndexError:
		pass

	# print("english: ", random_english_word)
	# print("french: ", random_french_word)


def known_word():
	try:
		english_words.remove(random_english_word)
		french_words.remove(random_french_word)
	except ValueError:
		pass

def show_word():
	random_words()
	global flip_timer
	window.after_cancel(flip_timer)
	canvas.itemconfig(card_title, text="French", fill="black")
	canvas.itemconfig(card_word, text=random_french_word, fill="black")
	canvas.itemconfig(card_background, image=card_front_image)
	flip_timer = window.after(3000, func=flip_card) 

def flip_card():
	canvas.itemconfig(card_title, text="English", fill="white")
	canvas.itemconfig(card_word, text=random_english_word, fill="white")
	canvas.itemconfig(card_background, image=card_back_image)

#--------------------- UI Setup --------------------

window = Tk()
window.title("Game of Flash Cards.")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

random_words()
flip_timer = window.after(3000, func=flip_card) 

canvas = Canvas(width=800, height=526)
card_front_image = PhotoImage(file="images/card_front.png") 
card_back_image = PhotoImage(file="images/card_back.png") 
card_background = canvas.create_image(400, 263, image=card_front_image)

card_title = canvas.create_text(400, 150, text="French", font=("Arial", 40, "italic"))
card_word = canvas.create_text(400, 263, text=random_french_word, font=("Arial", 60, "bold"))

canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=1, columnspan=2)

# Buttons
wrong_tick_image = PhotoImage(file="images/wrong.png")  
wrong_button = Button(image=wrong_tick_image, command=show_word)
wrong_button.grid(row=1, column=1)
wrong_button.config(highlightthickness=0)

right_tick_image = PhotoImage(file="images/right.png")  
right_button = Button(image=right_tick_image, command=known_word)
right_button.grid(row=1, column=2)
 
window.mainloop()
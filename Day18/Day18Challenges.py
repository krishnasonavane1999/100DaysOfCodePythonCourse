import turtle as t 
from turtle import Screen
import random

champ = t.Turtle()
champ.color("Blue")
champ.pensize("5")

t.colormode(255)

def give_random_color():
	r = random.randint(0, 255)
	g = random.randint(0, 255)
	b = random.randint(0, 255)

	random_color = (r, g, b)

	return random_color

def draw_square():
	for line in range(4):
		champ.forward(100)
		champ.right(90)





def draw_dashed_line():
	for line in range(20):
		champ.forward(10)
		champ.color("white")
		champ.forward(10)
		champ.color("Blue")




def generate_different_shapes():
	sides = 3
	for no_of_shapes in range(10):
		for shape in range(sides):
			champ.forward(100)
			champ.color(give_random_color())
			champ.right((360 / sides))
		sides += 1



def generate_random_walk():
	change_path = [0, 1, 0, 1, 1, 0]
	change_angle = [90, 270, 180, 90, 180, 270]
	champ.speed("fastest")
	champ.pensize(10)

	for steps in range(100):
		for step in range(10):
			champ.forward(30)
			champ.color(give_random_color())
			if change_path[random.randint(0, 5)]:
				champ.right(change_angle[random.randint(0, 5)])
			else:
				champ.left(change_angle[random.randint(0, 5)])


champ.pensize(1)
def draw_spinograph(gap_size):
	champ.speed("fastest")
	champ.pensize(2)
	for i in range((int(360 / gap_size))):
		champ.circle(100)
		champ.color(give_random_color())
		champ.setheading(champ.heading() + 10)

draw_spinograph(5)

# generate_random_walk()
# draw_square()
# draw_dashed_line()
# generate_different_shapes()








screen = Screen()
screen.exitonclick()

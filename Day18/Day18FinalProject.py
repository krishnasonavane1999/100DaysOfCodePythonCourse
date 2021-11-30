# import colorgram

# colors = colorgram.extract('hirstPainting.jpg', 30)

# rgb_colors = []

# for color in colors:
# 	r = color.rgb.r
# 	g = color.rgb.g
# 	b = color.rgb.b

# 	rgb_colors.append((r, g, b))

# print(rgb_colors)


color_list = [ (177, 78, 33), (198, 142, 35), (116, 155, 171), (124, 79, 98), (123, 175, 157), (226, 197, 130), (190, 88, 109), (12, 50, 64), (56, 39, 19), (41, 168, 128), (50, 126, 121), (199, 123, 143), (166, 21, 30), (224, 93, 79), (243, 163, 161), (38, 32, 34), (3, 25, 25), (80, 147, 169), (161, 26, 22), (21, 78, 90), (234, 167, 171), (171, 206, 190), (103, 127, 156), (165, 202, 210)]

import turtle as t
from turtle import Screen
import random

champ = t.Turtle()
t.colormode(255)

champ.penup()
champ.setheading(225)
champ.forward(300)
champ.setheading(0)

def give_random_color():
	random_color = color_list[random.randint(0, len(color_list) - 1)];
	return random_color

def draw_hirst_painting():

		champ.speed("fastest")
		champ.shape("turtle")
		champ.color("red")
		for _ in range(10):
			champ.dot(20, give_random_color())
			champ.penup()
			champ.forward(50)
		champ.dot(20, give_random_color())




		champ.left(90)
		champ.forward(50)
		# champ.dot(20, give_random_color())

		champ.left(90)

		for _ in range(10):
			champ.dot(20, give_random_color())
			champ.penup()
			champ.forward(50)
		champ.dot(20, give_random_color())


		champ.right(90)
		champ.forward(50)
		# champ.dot(20, give_random_color())
		champ.right(90)



		


no_of_lines = 5
while no_of_lines:
	draw_hirst_painting()
	no_of_lines -= 1


screen = Screen()
screen.exitonclick()
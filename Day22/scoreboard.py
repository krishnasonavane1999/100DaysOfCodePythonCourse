from turtle import *

class ScoreBoard(Turtle):
	def __init__(self):
		super().__init__()
		self.color("white")
		self.hideturtle()
		self.penup()
		self.l_score = 0
		self.r_score = 0
		self.goto(-10, 200)


	def inc_l_score(self):
		self.l_score += 1

	def inc_r_score(self):
		self.r_score += 1

	def show_score(self):
		self.clear()
		self.write(f"{self.l_score} {self.r_score}", align="center", font=("Courier", 80, "normal"))

		
from turtle import *

class Ball(Turtle):
	def __init__(self):
		super().__init__()
		self.color("white")
		self.shape("circle")
		self.penup()
		self.x_mov = 10
		self.y_mov = 10
		self.ball_speed = 0.1

	def move(self):
		new_x = self.xcor() + self.x_mov
		new_y = self.ycor() + self.y_mov
		self.goto(new_x, new_y)


	def bounce_y(self):
		self.y_mov *= -1

	def bounce_x(self):
		self.x_mov *= -1
		self.ball_speed *= 0.9

	def reset_ball_r(self):
		self.x_mov *= -1
		self.goto(0, 0)
		self.ball_speed = 0.1

	def reset_ball_l(self):
		self.x_mov *= -1
		self.goto(0, 0)
		self.ball_speed = 0.1

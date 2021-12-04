from turtle import *
from paddle import Paddle
from ball import Ball
import time
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)


position = (-350, 0)
ball_position = (0, 0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle(position)

new_ball = Ball()
score = ScoreBoard()

screen.listen()
screen.onkey(r_paddle.move_up, "Up")
screen.onkey(r_paddle.move_down, "Down")
screen.onkey(l_paddle.move_up, "w")
screen.onkey(l_paddle.move_down, "s")



game_is_on = True
l_score = r_score = 0

while game_is_on:
	screen.update()
	time.sleep(new_ball.ball_speed)
	new_ball.move()
	score.show_score()
	if new_ball.ycor() > 280 or new_ball.ycor() < -280:
		new_ball.bounce_y()

	if new_ball.distance(r_paddle) < 50 and new_ball.xcor() > 320 or new_ball.distance(l_paddle) < 50 and new_ball.xcor() < -320:
		new_ball.bounce_x()
		ball_speed -= 0.01

	if new_ball.xcor() > 380:
		new_ball.reset_ball_r()
		score.inc_l_score()

	elif new_ball.xcor() < -380:
		new_ball.reset_ball_l()
		score.inc_r_score()





screen.exitonclick()

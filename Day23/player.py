from turtle import *

STARTING_POSITION = (50, -250)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.shape("turtle")
        self.penup()
        self.goto(STARTING_POSITION)
        self.left(90)

    def move(self):
        self.forward(MOVE_DISTANCE)

    def game_won(self):
        self.write("You won!", move=False, align="center", font=("Arial", 30, "bold"))

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over!", move=False, align="center", font=("Arial", 30, "bold"))

    def player_reset(self):
        self.penup()
        self.goto(STARTING_POSITION)

    def is_at_finsh_line(self):
        if self.ycor() > 280:
            return True


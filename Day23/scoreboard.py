from turtle import *
FONT = ("Courier", 24, "normal")
ALIGN = "left"
MOVE = False
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(-280, 250)
        self.score = 1


    def show_score(self):

        self.write(f"Level: {self.score}", MOVE, ALIGN, FONT)

    def inc_score(self):
        self.clear()
        self.score += 1


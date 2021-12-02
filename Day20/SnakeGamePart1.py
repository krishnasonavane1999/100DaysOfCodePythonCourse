import time
from turtle import *
move_distance = 20
Up = 90
Down = 270
Left = 180
Right = 0

class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.snake_head = self.segments[0]

    def create_snake(self):
        for _ in range(3):
            champ = Turtle()
            champ.shape("square")
            champ.color("white")
            champ.penup()
            self.segments.append(champ)

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.snake_head.forward(move_distance)


    def up(self):
        if self.snake_head.heading() != Down:
            self.snake_head.setheading(Up)

    def down(self):
        if self.snake_head.heading() != Up:
            self.snake_head.setheading(Down)

    def left(self):
        if self.snake_head.heading() != Right:
            self.snake_head.setheading(Left)

    def right(self):
        if self.snake_head.heading() != Left:
            self.snake_head.setheading(Right)



screen = Screen()
screen.setup(width=600, height=600)
screen.title("Snake Game")
screen.bgcolor("black")
screen.tracer(0)

snake = Snake()
screen.listen()

screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


print(snake)

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()


screen.exitonclick()

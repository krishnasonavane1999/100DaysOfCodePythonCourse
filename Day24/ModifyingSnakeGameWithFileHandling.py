
import random
import time
from turtle import *
move_distance = 20
Up = 90
Down = 270
Left = 180
Right = 0

MOVE = False
ALIGNMENT = "center"
FONT = ("Arial", 14, "bold")

class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.snake_head = self.segments[0]

    def create_snake(self):
        for _ in range(3):
            self.add_segment(position)

    def add_segment(self, position):
        champ = Turtle("square")
        champ.penup()
        champ.color("white")
        self.segments.append(champ)

    def extend_snake(self):
        self.add_segment(self.segments[-1].position())


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

    def detect_collision_with_food(self):
        if self.snake_head.distance(food) < 15:
            return True

    def detect_collision_with_wall(self):
        if self.snake_head.xcor() > 295 or self.snake_head.xcor() < -295 or self.snake_head.ycor() > 295 or \
                self.snake_head.ycor() < -295:
            return True

    def detect_collision_with_tail(self):
        for segment in self.segments:
            if segment == self.snake_head:
                pass
            elif self.snake_head.distance(segment) < 10:
                return True

    def reset_game(self):
        for segment in self.segments:
            segment.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()
        self.snake_head = self.segments[0]



class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.7, stretch_wid=0.7)
        self.color("red")
        self.speed("fastest")
        self.refresh_food()

    def refresh_food(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.count = 0
        with open("highest_score.txt", "r") as data:
            self.highest_score = int(data.read())
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.updated_scoreboard()
        self.hideturtle()

    def increase_score(self):
        self.count += 1

    def keep_highest_score(self):
        if self.count > self.highest_score:
            self.highest_score = self.count 

        with open("highest_score.txt", "w") as file:
            file.write(str(self.highest_score))

    def updated_scoreboard(self):
        self.clear()
        
        self.write(f"Score: {self.count}  Highest Score: {self.highest_score}", MOVE, ALIGNMENT, FONT)


    def set_score_to_zero(self):
        self.count = 0

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Snake Game")
screen.bgcolor("black")
screen.tracer(0)

snake = Snake()
food = Food()
score = ScoreBoard()



screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


print(snake)

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    snake.move()
    if snake.detect_collision_with_food():
        snake.extend_snake()
        score.increase_score()
        score.updated_scoreboard()
        food.refresh_food()


    if snake.detect_collision_with_wall():
        score.keep_highest_score()
        score.updated_scoreboard()
        score.set_score_to_zero()
        snake.reset_game()

    if snake.detect_collision_with_tail():
        score.keep_highest_score()
        score.updated_scoreboard()
        score.set_score_to_zero()
        snake.reset_game()


screen.exitonclick()

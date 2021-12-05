import time
import random
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

champ = Player()
car = CarManager()
scoreboard = Scoreboard()

champ.speed("fastest")
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    screen.listen()
    screen.onkey(champ.move, "Up")
    scoreboard.show_score()
    if champ.is_at_finsh_line():
        champ.game_won()
        champ.player_reset()
        car.next_level()
        scoreboard.inc_score()
        # game_is_on = False
    
    car.create_car()
    car.move()

    for vehicle in car.all_cars:
        if champ.distance(vehicle) < 20:
            champ.color("red")
            champ.game_over()
            game_is_on = False



screen.exitonclick()
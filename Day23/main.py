from turtle import Screen
from player import Player
from scoreboard import Scoreboard
from carmanager import CarManager
import random
import time

screen = Screen()
screen.setup(600,600)
screen.bgcolor("white")
screen.title("Turtle Crossing")
screen.tracer(0)
screen.listen()
player = Player()
score = Scoreboard()
car = CarManager()
screen.onkey(key="Up", fun=player.move)

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1) #Momentan, trebuie actualizat dupa
    car.move_cars()
    if player.ycor() > 280:
        score.level_up()
        player.reset_position()
        car.level_up_speed()
        car.reset_cars()
    if random.randint(1,5) == 1:
        car.create_car()
    for single_car in car.all_cars:
        if player.distance(single_car) < 20:
            score.game_over()
            game_is_on = False

screen.exitonclick()
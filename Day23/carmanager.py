from turtle import Turtle
import random

START_X = 300
POZITII_GENERARE_CAR= [-240, -220, -200, -180, -160, -140, -120, -100, -80, -60, -40, -20, 0, 20, 40, 60, 80, 100, 120, 140, 160, 180, 200, 220, 240]

COLORS=["green", "blue", "yellow", "purple", "pink", "orange", "brown", "red"]

class CarManager:
    def __init__(self):
        self.all_cars = []
        self.car_speed = 5

    def create_car(self):
        random_y = random.choice(POZITII_GENERARE_CAR)
        new_car = Turtle()
        new_car.shape("square")
        new_car.shapesize(stretch_wid=1, stretch_len=2)
        new_car.penup()
        new_car.color(random.choice(COLORS))
        new_car.goto(x = START_X, y = random_y)
        self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car = car.goto(car.xcor() - self.car_speed, car.ycor())

    def level_up_speed(self):
        self.car_speed += 2

    def reset_cars(self):
        for car in self.all_cars:
            car.hideturtle()
        self.all_cars = []

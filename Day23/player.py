from turtle import Turtle

STARTING_POSITION = (0, -280)
class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.color("black")
        self.reset_position()
        self.setheading(90)

    def move(self):
        new_y=self.ycor() + 10
        self.goto(self.xcor(),new_y)

    def reset_position(self):
        self.goto(STARTING_POSITION)
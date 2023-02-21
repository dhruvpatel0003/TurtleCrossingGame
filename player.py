from turtle import Turtle

class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.hideturtle()
        self.shapesize(1,1)
        self.goto(0,-270)
        self.left(90)
        self.showturtle()

    def move_player(self):
        self.forward(10)
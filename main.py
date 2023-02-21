import time
from turtle import Turtle, Screen
from object import Object
from player import Player
from level import LevelUpdate
from home import go_Home
from tkinter import *

def function():

    turtle = Turtle()
    turtle.hideturtle()
    screen = Screen()
    screen.clear()
    screen.bgcolor("white")
    screen.setup(600,600)
    flage = True
    new_player = Player()
    screen.tracer(0)
    screen.title("Road Crossing")
    screen.listen()
    screen.onkey(new_player.move_player,"Up")
    screen.onkey(function,"r")
    new_object = Object()
    show_level = LevelUpdate()
    speed = 0.1
    show_level.update_score()

    while flage:

                time.sleep(speed)
                screen.update()
                new_object.create()
                new_object.move(new_player.position(),new_player.xcor(),new_player.ycor())
                if not new_object.back():
                    print("Inside")
                    go_Home(new_player)
                    break
                if new_player.ycor() > 260:
                    show_level.update_score()
                    go_Home(new_player)
                    speed *= 0.9

    screen.exitonclick()


function()


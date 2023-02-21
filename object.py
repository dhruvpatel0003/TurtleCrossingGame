from turtle import Turtle
import random as r
import time
# screen = Screen()
COLOR = ['red','black','green']

class Object():

    def __init__(self):
        # super().__init__()
        self.list = []
        self.flage = True
        self.b = True

    def create(self):
        go_ahead = r.randint(1,6)
        if go_ahead == 1:
            new_car = Turtle()
            # new_car.hideturtle()
            new_car.shape("square")
            new_car.color(r.choice(COLOR))
            new_car.penup()
            new_car.shapesize(1.5, 3.5)
            y_cor = r.randint(-230, 230)
            new_car.goto(350, y_cor)
            self.list.append(new_car)
            # new_car.showturtle()

    def move(self,x_distance,x,y):
        turtle = Turtle()
        turtle.hideturtle()
        for car in self.list:
                if self.flage:
                    car.backward(10)
                    # time.sleep(0.1)
                    # print("x,x1", car.xcor(),x)
                    if car.distance(x_distance) < 20 and x - car.xcor() < 50 :
                        turtle.write("Game Over!",align="center",font=("Arial", 20, "bold"))
                        self.game_over()
                        self.flage = False
                    elif (y - car.ycor() == -20 and car.distance(x_distance) < 40) :
                        self.game_over()
                        self.flage = False
                else:
                    self.b = False
                    break


    def game_over(self):
        print("Game over")
        self.flage = False

    def back(self):
        if not self.b:
            return False
        else:
            return True
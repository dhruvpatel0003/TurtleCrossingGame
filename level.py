from turtle import Turtle

class LevelUpdate(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 1
        self.hideturtle()

    def update_score(self):
        self.penup()
        self.goto(-220,250)
        # self.showturtle()
        self.clear()
        # self.showturtle()
        self.write(f"Level : {self.score}",align="center",font=("Arial",20,"bold"))
        self.score += 1


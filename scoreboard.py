import time
from turtle import Turtle


ALIGNMENT = "center"
FONT = ("Menlo", 16, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("/Users/diegoo.guajardoo/Desktop/data.txt", mode="r") as d:
            self.high_score = int(d.read())
        self.color("white")
        self.penup()
        self.sety(275)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(arg=f"Score: {self.score} High Score: {self.high_score}", move=False, align=ALIGNMENT, font=FONT)

    def reset_high_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("/Users/diegoo.guajardoo/Desktop/data.txt", mode="w") as file:
                file.write(str(self.score))
        self.score = 0
        self.update_scoreboard()

    def add_point(self):
        self.score += 1
        self.update_scoreboard()

    def teletransport_message(self):
        self.penup()
        self.sety(-40)
        self.hideturtle()
        self.write(arg="TELETRANSPORTATION!", align="center", font=("Menlo", 16, "normal"))
        time.sleep(1)
        self.clear()
        self.sety(275)

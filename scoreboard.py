from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Menlo", 16, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.sety(275)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(arg=f"Score: {self.score}", move=False, align=ALIGNMENT, font=FONT)

    def add_point(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def game_over(self):
        self.penup()
        self.sety(0)
        self.hideturtle()
        self.write(arg="GAME OVER.", align="center", font=("Menlo", 16, "normal"))


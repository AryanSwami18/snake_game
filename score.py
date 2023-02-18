from turtle import Turtle

SCORE = 0


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(0, 270)
        self.update_score()
        self.hideturtle()

    def update_score(self):
        global SCORE
        self.clear()
        self.color("white")
        self.write(f"score:{SCORE}", align="center", font=("arial", 15, "normal"))
        SCORE += 1

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", align="center", font=("arial", 15, "normal"))

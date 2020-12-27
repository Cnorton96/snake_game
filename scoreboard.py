from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.color("blue")
        self.penup()
        self.goto(0, 270)
        self.updated_board()
        self.hideturtle()

    def updated_board(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align="center", font=("Arial", 26, "normal"))

    def score_increased(self):
        self.score += 1
        self.updated_board()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.updated_board()



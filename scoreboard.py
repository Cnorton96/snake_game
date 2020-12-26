from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.updated_board()
        self.hideturtle()

    def updated_board(self):
        self.write(f"Score: {self.score}", align="center", font=("Arial", 26, "normal"))

    def score_increased(self):
        self.score += 1
        self.clear()
        self.updated_board()

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over.", align="center", font=("Arial", 26, "normal"))

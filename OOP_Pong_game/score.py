from turtle import Turtle
FONT = "Courier", 14, "normal"


class Scoreboard(Turtle):
    def __init__(self, x_cor):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(x_cor, 275)
        self.score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}", font=FONT)

    def add_score(self):
        self.score += 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(-50, 0)
        self.write(f"GAME OVER", font=FONT)

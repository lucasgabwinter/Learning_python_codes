from turtle import Turtle
MOVE_DISTANCE = 30


class Paddle(Turtle):
    def __init__(self, x_cor_, y_cor_):
        super().__init__()
        self.penup()
        self.color("white")
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(x_cor_, y_cor_)

    def go_up(self):
        temp_y = self.ycor()
        self.goto(x=self.xcor(), y=temp_y + MOVE_DISTANCE)

    def go_down(self):
        temp_y = self.ycor()
        self.goto(x=self.xcor(), y=temp_y - MOVE_DISTANCE)

from ball import Ball
from turtle import Screen
from paddle import Paddle
from score import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.title("Pong game")
screen.bgcolor("black")
screen.tracer(0)
p1_score = Scoreboard(100)
p2_score = Scoreboard(-200)
p2 = Paddle(-350, 0)
p1 = Paddle(350, 0)
b1 = Ball()

screen.listen()
screen.onkey(p1.go_up, "Up")
screen.onkey(p1.go_down, "Down")
screen.onkey(p2.go_up, "W")
screen.onkey(p2.go_down, "S")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    b1.move()
    # Detect collision with wall
    if b1.ycor() >= 285 or b1.ycor() <= -285:
        b1.bounce_y()

    # Detect collision with paddles
    if (b1.distance(p1) < 50 and b1.xcor() > 330) or (b1.distance(p2) < 50 and b1.xcor() < -330):
        b1.bounce_x()
    # Detect when the ball passes away to the right
    elif b1.xcor() >= 420:
        p2_score.add_score()
        b1.x_move = b1.x_move * -1
        b1.reset_position()
    # Detect when the ball passes away to the left
    elif b1.xcor() <= -420:
        p1_score.add_score()
        b1.x_move = b1.x_move * -1
        b1.reset_position()
    if p1_score.score == 2 or p2_score.score == 2:
        p1_score.game_over()
        game_is_on = False

screen.exitonclick()

from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

scoreboard = Scoreboard()
right_paddle = Paddle((350, 0))
left_paddle = Paddle((-350, 0))
ball = Ball()

screen.listen()
screen.onkeypress(right_paddle.up, "Up")
screen.onkeypress(right_paddle.down, "Down")
screen.onkeypress(left_paddle.up, "w")
screen.onkeypress(left_paddle.down, "s")

game_on = True
ball_speed = 0.065
while game_on:
    time.sleep(ball_speed)
    screen.update()
    ball.move()

    # Detect ball collision with top or bottom walls
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.y_bounce()

    # Detect ball collision with paddle
    if (ball.distance(right_paddle) < 50 and ball.xcor() > 325) or \
            (ball.distance(left_paddle) < 50 and ball.xcor() < -325):
        ball.x_bounce()
        ball_speed -= 0.005

    # Detect if ball is missed by either player, change score, and reset ball
    if ball.xcor() > 400 or ball.xcor() < -400:
        if ball.xcor() > 400:
            scoreboard.change_score("l")
        else:
            scoreboard.change_score("r")
        ball.goto(0, 0)
        ball_speed = 0.065
        ball.x_bounce()

screen.exitonclick()

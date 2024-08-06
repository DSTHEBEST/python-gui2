from turtle import Turtle, Screen
from paddle import Paddle, Ball
import time
from score import ScoreBoard
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.tracer(0)
ball = Ball()
board = ScoreBoard()

pad = Paddle((-350, 0))

pad2 = Paddle((350, 0))

screen.listen()
screen.onkey(pad2.going_up, "Up")
screen.onkey(pad2.going_down, "Down")
screen.onkey(pad.going_up, "w")
screen.onkey(pad.going_down, "s")

is_game_on = True

while is_game_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(pad2) < 50 and ball.xcor() > 320 or ball.distance(pad) < 50 and ball.xcor() < -320:
        ball.bounce_x()
    elif ball.xcor() > 340:
        ball.reset_ball_x()

        board.l_point()

    elif ball.xcor() < -340:
        ball.reset_ball_y()
        board.r_point()




screen.exitonclick()

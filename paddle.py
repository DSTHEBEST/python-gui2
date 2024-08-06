from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid=3, stretch_len=-1)
        self.goto(position)

    def going_up(self):
        x = self.ycor() + 40
        self.goto(self.xcor(), x)

    def going_down(self):
        y = self.ycor() - 40
        self.goto(self.xcor(), y)


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.xx_move = -10
        self.x = 0
        self.y = 0

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1

    def reset_ball_x(self):
        self.goto(0,0)
        self.bounce_x()

    def reset_ball_y(self):
        self.goto(0, 0)
        self.bounce_y()



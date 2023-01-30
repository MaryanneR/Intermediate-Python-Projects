from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.return_to_start()
        self.setheading(90)

    def move_forward(self):
        new_y = self.ycor() + MOVE_DISTANCE
        self.goto(self.xcor(), new_y)

    def successful_crossing(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False

    def return_to_start(self):
        self.goto(STARTING_POSITION)

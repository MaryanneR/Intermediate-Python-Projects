from turtle import Turtle

SCOREBOARD_X = -230
SCOREBOARD_Y = 270
ALIGNMENT = "center"
FONT = ("Courier", 18, "normal")
GAME_OVER_FONT = ("Courier", 40, "bold")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.current_level = 0
        self.color("black")
        self.penup()
        self.goto(SCOREBOARD_X, SCOREBOARD_Y)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Level: {self.current_level}", move=False, align=ALIGNMENT, font=FONT)

    def change_score(self):
        self.current_level += 1
        self.clear()
        self.update_scoreboard()

    def game_over_message(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", move=False, align=ALIGNMENT, font=GAME_OVER_FONT)
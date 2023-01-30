from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 20, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.l_player_score = 0
        self.r_player_score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 270)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"{self.l_player_score}  |  {self.r_player_score}", move=False, align=ALIGNMENT, font=FONT)

    def change_score(self, player_point):
        if player_point == "l":
            self.l_player_score += 1
        else:
            self.r_player_score += 1
        self.clear()
        self.update_scoreboard()

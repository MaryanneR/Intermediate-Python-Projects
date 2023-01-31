from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 14, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.current_score = 0
        with open("data") as data:
            self.high_score = int(data.read())
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.current_score}  |  High Score: {self.high_score}", move=False, align=ALIGNMENT,
                   font=FONT)

    def change_score(self):
        self.current_score += 1
        self.update_scoreboard()

    def reset(self):
        if self.current_score > self.high_score:
            self.high_score = self.current_score
            with open("data", mode="w") as data:
                data.write(f"{self.high_score}")
        self.current_score = 0
        self.update_scoreboard()

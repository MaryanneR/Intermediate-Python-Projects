import turtle
import pandas as pd
import sys

ALIGNMENT = "center"
POP_UP_FONT = ("Times New Roman", 8, "normal")
FINAL_FONT = ("Times New Roman", 30, "bold")

screen = turtle.Screen()
screen.title("U.S. States Game")
screen.setup(width=725, height=491)
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# # Collect state x,y locations
# def get_mouse_click_coor(x, y):
#     print(x, y)
#
#
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()

data = pd.read_csv("50_states.csv")
state_list = data.state.to_list()

state_count = 0
guessed_states = []
missing_states = []
header_message = "Guess a State"
body_message = "Enter another state's name: "

while state_count <= 50:
    if state_count == 50:
        ft = turtle.Turtle()
        ft.hideturtle()
        ft.penup()
        ft.write("Congratulations!\nYou've guessed all 50 states correctly!", align=ALIGNMENT, font=FINAL_FONT)

    answer = screen.textinput(f"{header_message}", body_message).title()

    if answer == "Exit":
        for state in state_list:
            if state not in guessed_states:
                missing_states.append(state)
        learning_data = pd.DataFrame(missing_states)
        learning_data.to_csv("states_to_learn.csv")
        sys.exit()

    if answer in state_list and answer not in guessed_states:
        x_cor = int(data[data.state == answer].x)
        y_cor = int(data[data.state == answer].y)

        guessed_states.append(answer)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.goto(x_cor, y_cor)
        t.write(f"{answer}", align=ALIGNMENT, font=POP_UP_FONT)

        state_count += 1
        header_message = f"{state_count}/50 states guessed"

turtle.mainloop()

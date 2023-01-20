import turtle as t
import random

screen = t.Screen()
screen.colormode(255)

color_list = [(40, 3, 179), (85, 251, 187), (224, 151, 108), (158, 3, 80), (5, 211, 91), (4, 139, 66), (240, 43, 125),
              (112, 103, 240), (251, 250, 57), (165, 121, 239), (47, 239, 55), (185, 181, 247), (209, 102, 6),
              (37, 33, 250), (219, 117, 168), (140, 2, 1), (249, 37, 34), (83, 245, 251), (202, 33, 111), (25, 2, 106),
              (39, 113, 143), (104, 2, 52), (10, 209, 217), (226, 167, 206), (222, 121, 16), (2, 115, 34), (103, 1, 1),
              (233, 172, 167), (251, 8, 23), (0, 114, 120), (1, 250, 237), (255, 7, 5)]


def painting():
    for i in range(0, 11):
        tim.color(random.choice(color_list))
        tim.begin_fill()
        tim.circle(7.5)
        tim.end_fill()
        tim.penup()
        tim.forward(50)


def direction(row_num):
    if row_num == 10:
        return
    elif row_num == 0 or row_num % 2 == 0:
        tim.left(90)
        tim.forward(66)
        tim.left(90)
        tim.forward(50)
    else:
        tim.right(90)
        tim.forward(36)
        tim.right(90)
        tim.forward(50)


tim = t.Turtle()
tim.hideturtle()
tim.speed(0)

# Put tim in starting position
tim.penup()
tim.right(180)
tim.forward(300)
tim.left(90)
tim.forward(240)
tim.left(90)
tim.forward(50)

row_number = 0
for i in range(0, 10):
    painting()
    direction(row_number)
    row_number += 1

screen.exitonclick()

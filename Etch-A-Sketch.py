from turtle import Turtle, Screen

pointer = Turtle()
screen = Screen()


def movement(k):
    if k == "w":
        pointer.forward(10)
    elif k == "s":
        pointer.backward(10)
    elif k == "a":
        pointer.left(10)
    elif k == "d":
        pointer.right(10)
    else:
        pointer.reset()


screen.listen()

for letter in ("a", "s", "w", "d", "c"):
    screen.onkey(lambda letter=letter: movement(letter), str(letter))

screen.exitonclick()

from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
start_race = False
users_turtle = screen.textinput(title="Choose your turtle racer", prompt="Which turtle do you think will win? "
                                                                         "red/orange/yellow/green/blue/purple : ")

turtle_racers = []
t_colors = ["red", "orange", "yellow", "green", "blue", "purple"]
starting_y = 75

for num in range(0, 6):
    racer = Turtle(shape="turtle")
    racer.penup()
    racer.color(t_colors[num])
    racer.goto(x=-230, y=starting_y)
    starting_y -= 30
    turtle_racers.append(racer)

if users_turtle:
    start_race = True

while start_race:

    for turtle in turtle_racers:
        if turtle.xcor() > 230:
            start_race = False
            winner = turtle.pencolor()
            if winner == users_turtle.lower():
                print(f"The {winner} turtle has won the race! Congratulations! You've won!")
            else:
                print(f"The {winner} turtle has won the race. Try again!")

        rand_speed = random.randint(0, 10)
        turtle.forward(rand_speed)

screen.exitonclick()

import random
from turtle import Screen, Turtle

screen = Screen()
screen.setup(width=500, height=400)


user_bet = screen.textinput(title='Make your bet', prompt="Which turtle will win the race? Enter the color: ")

colors = ['blue', 'red', 'green', 'purple', 'orange', 'pink']
turtles = []

for n in range(6):
    turtle = Turtle(shape='turtle')
    turtle.color(colors[n])
    turtle.penup()
    turtle.goto(x=-235, y=-75 + (n * 25))
    turtles.append(turtle)

is_race_on = False
winning_color = ''

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in turtles:
        turtle.forward(random.randint(1, 6))

    for turtle in turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            turtle.goto(0, 0)

print(f'The winning turtle was {winning_color}')
print(f'This means you {"won" if winning_color == user_bet else "lost"}')
screen.exitonclick()






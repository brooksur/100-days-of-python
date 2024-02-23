from turtle import Turtle, Screen

turtle = Turtle()
screen = Screen()

turtle.shape('turtle')
turtle.color('blue')

def square(paces):
    for _ in range(4):
        turtle.forward(paces)
        turtle.left(90)

def dash(paces):
    up_or_down = 'down'
    for _ in range(25):
        turtle.forward(paces)
        if up_or_down == 'up':
            turtle.down()
            up_or_down = 'down'
        else:
            turtle.up()
            up_or_down = 'up'


dash(5)


screen.exitonclick()


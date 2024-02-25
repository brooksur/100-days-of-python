import random
from turtle import Turtle, Screen, colormode
import colorgram

colormode(255)

t = Turtle()
t.width(2)
screen = Screen()


def hurst_color_palette():
    colors = colorgram.extract('spots.jpg', 50)
    colors_rgb = []

    for color in colors:
        rgb = color.rgb  # RGB values
        if (rgb[0] + rgb[1] + rgb[2]) < 700:
            colors_rgb.append(rgb)

    return colors_rgb


def square(paces):
    for _ in range(4):
        t.forward(paces)
        t.left(90)


def dash(paces, iterations):
    up_or_down = 'down'
    for _ in range(iterations):
        t.forward(paces)
        if up_or_down == 'up':
            t.down()
            up_or_down = 'down'
        else:
            t.up()
            up_or_down = 'up'


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)


def draw_shape(num_sides, side_length, line_color):
    t.color(line_color)
    turn_angle = 360 / num_sides
    for _ in range(num_sides):
        t.forward(side_length)
        t.left(turn_angle)


def random_walk():
    for _ in range(1000):
        t.setheading((random.choice([0, 90, 180, 270])))
        t.color(random_color())
        t.forward(25)


def circle():
    for _ in range(36):
        t.color(random_color())
        t.circle(100)
        t.left(10)


def hurst_painting():
    t.hideturtle()
    colors = hurst_color_palette()

    for i in range(10):
        t.penup()
        t.goto(0, i * 50)
        for j in range(10):
            t.pendown()
            t.dot(20, random.choice(colors))
            t.penup()
            if j < 9:
                t.forward(50)


hurst_painting()

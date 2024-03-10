from turtle import Turtle, Screen


class Sketch:
    def __init__(self):
        s = Screen()
        t = Turtle()

        self.t = t
        self.s = s

        s.listen()

        s.onkey(self.forward, 'w')
        s.onkey(self.back, 's')
        s.onkey(self.left, 'a')
        s.onkey(self.right, 'd')

        s.exitonclick()

    def forward(self):
        self.t.forward(10)

    def back(self):
        self.t.backward(10)

    def left(self):
        self.t.setheading(self.t.heading() + 10)

    def right(self):
        self.t.setheading(self.t.heading() - 10)

    def clear(self):
        t = self.t
        t.clear()
        t.penup()
        t.home()
        t.pendown()


sketch = Sketch()

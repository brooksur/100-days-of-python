from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]

RIGHT = 0
UP = 90
LEFT = 180
DOWN = 270


class Snake:

    def __init__(self):
        self.segments = []
        self.head = None
        self.create_snake()

    def create_snake(self):
        for pos in STARTING_POSITIONS:
            self.add_segment(pos)
        self.head = self.segments[0]

    def add_segment(self, position):
        new_segment = Turtle()
        new_segment.shape('square')
        new_segment.color('white')
        new_segment.penup()
        new_segment.goto(position[0], position[1])
        self.segments.append(new_segment)

    def reset(self):
        for seg in self.segments:
            seg.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()

    def extend(self):
        last_segment_position = self.segments[-1].position()
        self.add_segment(last_segment_position)

    def change_direction(self, direction):
        def change():
            cur_direction = self.segments[0].heading()

            if direction == 'right' and cur_direction != LEFT:
                self.segments[0].setheading(RIGHT)
            elif direction == 'up' and cur_direction != DOWN:
                self.segments[0].setheading(UP)
            elif direction == 'left' and cur_direction != RIGHT:
                self.segments[0].setheading(LEFT)
            elif direction == 'down' and cur_direction != UP:
                self.segments[0].setheading(DOWN)

        return change

    def move(self):
        segments = self.segments

        for seg_num in range(len(segments) - 1, 0, -1):
            new_x = segments[seg_num - 1].xcor()
            new_y = segments[seg_num - 1].ycor()
            segments[seg_num].goto(new_x, new_y)

        self.head.forward(20)

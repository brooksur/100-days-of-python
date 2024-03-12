from turtle import Screen
import time
from snake import Snake

screen = Screen()
snake = Snake()

screen.setup(width=1000, height=1000)
screen.bgcolor('black')
screen.title('Snake 🐍')
screen.tracer(0)

screen.listen()

screen.onkey(snake.change_direction('up'), 'Up')
screen.onkey(snake.change_direction('down'), 'Down')
screen.onkey(snake.change_direction('left'), 'Left')
screen.onkey(snake.change_direction('right'), 'Right')

game_is_on = True

while game_is_on:
    snake.move()
    screen.update()
    time.sleep(0.1)


screen.exitonclick()

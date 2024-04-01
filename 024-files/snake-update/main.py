from time import sleep
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.setup(width=600, height=600)
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
    sleep(0.09)

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.increase_score()
        snake.extend()

    # Detect collision with wall
    if snake.head.xcor() < -280 or snake.head.xcor() > 280 or snake.head.ycor() < -280 or snake.head.ycor() > 280:
        scoreboard.reset()
        snake.reset()

    # Detect collision with tail
    for seg in snake.segments[1:]:
        if snake.head.distance(seg) < 10:
            scoreboard.reset()
            snake.reset()

screen.exitonclick()

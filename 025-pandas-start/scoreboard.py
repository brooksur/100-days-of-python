from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.penup()
        self.hideturtle()
        self.score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(0, 300)
        self.write(f'{self.score} / 50', align='center', font=('Courier', 24, 'normal'))

    def game_over(self):
        self.clear()
        self.goto(0, 300)
        self.write(f'Game Over!\nYou guessed {self.score} out of 50 states', align='center', font=('Courier', 24, 'normal'))

    def add_one(self):
        self.score += 1
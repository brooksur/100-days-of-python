from turtle import Turtle

ALIGNMENT = 'center'
FONT = ("Courier", 12, "normal")
FILE = 'data.txt'

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open(FILE) as data:
            self.high_score = int(data.read())
        self.color("white")  # Set the color of the text
        self.penup()  # Ensure that the turtle's movement does not draw lines
        self.goto(0, 250)  # Position the scoreboard at the top of the screen
        self.hideturtle()  # Hide the turtle icon
        self.update_scoreboard()  # Call this method to display the initial score

    def update_scoreboard(self):
        self.clear()  # Clear the previous score before updating it
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)  # Display the new score

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()  # Update the scoreboard to reflect the new score

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open(FILE, mode='w') as data:
                data.write(f'{self.high_score}')
        self.score = 0
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write('GAME OVER', align=ALIGNMENT, font=FONT)

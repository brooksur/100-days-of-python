import turtle
import pandas
from scoreboard import Scoreboard

# Setup states frame
states_frame = pandas.read_csv('50_states.csv')

# Setup screen
states_img = 'blank_states_img.gif'
screen = turtle.Screen()
screen.bgcolor('black')
screen.title('US States Game')
screen.addshape(states_img)
map_img = turtle.Turtle()
map_img.shape(states_img)

# Game
scoreboard = Scoreboard()
run_game = True
answers = []
while run_game:
    if len(answers) < 50:
        # Get input from user
        answer = screen.textinput(title="Guess the state", prompt="What's the state's name?")
        answer = answer.lower()

        # Check for exit
        if answer == 'exit':
            missing_states = states_frame[~states_frame['state'].isin(answers)]
            missing_states.to_csv('missing_states.csv')
            run_game = False
            scoreboard.game_over()


        state_row = states_frame.loc[states_frame['state'].str.lower() == answer]

        # Handle correct answer
        if not state_row.empty and answer not in answers:
            scoreboard.add_one()
            scoreboard.update_scoreboard()
            answers.append(answer)
            state_label = turtle.Turtle()
            state_label.penup()
            state_label.hideturtle()
            print(state_row.iloc[:, [1, 2]].values)
            state_label.goto(state_row.iloc[:, [1, 2]].values[0])
            state_label.write(answer.title(), align='center')
    else:
        print('You win!')

screen.exitonclick()

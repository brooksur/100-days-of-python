import turtle
import pandas

# Globals
image = 'blank_states_img.gif'
states = pandas.read_csv('50_states.csv')

# Setup screen
screen = turtle.Screen()
screen.title('US States Game')
screen.addshape(image)

# Setup map
map = turtle.Turtle()
map.shape(image)

# Game
run_game = True
answers = []
while run_game:
    state = screen.textinput(title="Guess the state", prompt="What's the state's name?")
    state = state.lower()
    state_row = states.loc[states['state'].str.lower() == state]
    if not state_row.empty:
        answers.append(state)
        states.drop(state_row.index)
        state_label = turtle.Turtle()
        state_label.write(state, True)
        state_label.goto(state_row[1], state_row[2])
    run_game = False


screen.exitonclick()

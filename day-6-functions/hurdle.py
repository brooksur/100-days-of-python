# url: https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%201&url=worlds%2Ftutorial_en%2Fhurdle1.json


# move()
# turn_left()
def move():
    print('move')


def turn_left():
    print('turn_left')


def turn_right():
    turn_left()
    turn_left()
    turn_left()


def hurdle():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()


hurdles = 6
while hurdles != 0:
    hurdle()
    hurdles -= 1
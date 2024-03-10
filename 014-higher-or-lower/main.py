import random
from art import logo, vs
from game_data import data

print(logo)
print('Welcome to higher or lower!')

high_score = 0

def game():
    global high_score

    accounts = list(data)

    def get_account():
        account_index = random.randrange(len(accounts))
        return accounts.pop(account_index)

    print(f"The high score is {high_score}\n")

    score = 0
    choices = [get_account(), get_account()]


    is_playing = True

    while is_playing:
        choice_1 = choices[0]
        choice_2 = choices[1]
        choice_2.follo
        user_choice = user_choice = input(
            f'Does {choice_1["name"]} have more or less followers than {choice_2["name"]}? (m/l) \n'
        ).lower()

        is_more = choice_1['follower_count'] > choice_2['follower_count']

        if (user_choice == 'm' and is_more):
            score += 1
        elif (user_choice == 'l' and not is_more):
            score += 1
        else:
            is_playing = False

        choices[0] = choice_2
        choices[1] = get_account()

    print(f'Good game! Thanks for playing. You scored {score}.')

    if (score > high_score):
        high_score = score

def main():
  is_playing = True

  while is_playing:
      game()
      is_playing = input("Play again? 'y/n'") == 'y'

main()

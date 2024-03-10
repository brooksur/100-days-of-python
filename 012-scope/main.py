import random

def get_attempts(difficulty):
    if (difficulty == "easy"):
        return 10
    else:
        return 5

def get_guess():
    user_choice = int(input('Please choose a number between 1 and 100: '))
    return user_choice

def number_guessing_game():
    number = random.randint(1, 100)
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    attempts = get_attempts(difficulty)

    is_guessing = True
    
    while is_guessing and attempts != 0:
        guess = get_guess()

        if guess == number:
            is_guessing = False
        elif guess > number:
            print("Too high.")
            attempts -= 1
        elif guess < number:
            print("Too low.")
            attempts -= 1

    if attempts == 0:
        print("You've run out of guesses, you lose.")

    else:
        print(f"You got it! The answer was {number}.")

is_playing = True

while is_playing:
    number_guessing_game()
    is_playing = input('Do you want to play again? Type "y" or "n": ') == 'y'
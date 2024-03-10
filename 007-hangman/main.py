import random
import art
import words

chosen_word = random.choice(words.list)

print(f'Pssst, the solution is {chosen_word}.')

print(art.logo)
guesses = []
display = []

for letter in chosen_word:
    display += '_'

has_won = False
lives = 6

while not has_won and lives > 0:
    guess = input("Guess a letter: ").lower()

    if guess in guesses:
        print(f"\nYou have already guessed {guess}\n")
    else:
        guesses += guess

        correct_guess = False

        for n in range(len(chosen_word)):
            if chosen_word[n] == guess:
                display[n] = guess
                correct_guess = True

        if not correct_guess:
            lives -= 1
            print(
                f"You guessed {guess}, that's not in the word. You lose a life."
            )

        print(art.stages[6 - lives])
        print(f"{' '.join(display)}\n\n")

        contains_underscore = False

        for letter in display:
            if letter == '_':
                contains_underscore = True

        if not contains_underscore:
            has_won = True

if has_won:
    print("You win!")
else:
    print("You lose!")

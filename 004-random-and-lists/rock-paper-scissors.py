import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

opts = [rock, paper, scissors]

user_input = input('Choose rock, paper, or scissors: ').lower()
user_index = 0

if user_input == 'rock':
  user_index = 0
elif user_input == 'paper':
  user_index = 1
elif user_input == 'scissors':
  user_index = 2
else:
  print('Invalid input')

computer_index = random.randint(0, 2)

print('You chose:')
print(opts[user_index])

print('Computer chose:')
print(opts[computer_index])

if user_index == computer_index:
  print('Draw')
elif user_index == 0 and computer_index == 2:
  print('You win')
elif user_index == 1 and computer_index == 0:
  print('You win')
elif user_index == 2 and computer_index == 1:
  print('You win')
else:
  print('You lose')


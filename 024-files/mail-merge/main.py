with open('Input/Letters/starting_letter.txt') as starting_letter_file:
    starting_letter = starting_letter_file.read()

with open('Input/Names/invited_names.txt') as invited_names_file:
    invited_names = []
    for name in invited_names_file:
        invited_names.append(name.strip())

invitations = []

for name in invited_names:
    with open(f'Output/ReadyToSend/{name}_invitation.txt', 'w') as new_file:
        new_file.write(starting_letter.replace('[name]', name))





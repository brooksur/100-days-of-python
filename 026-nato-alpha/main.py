import pandas

alphabet = pandas.read_csv('nato_phonetic_alphabet.csv')
alphabet_dict = {row.letter.lower(): row.code for (key, row) in alphabet.iterrows()}


def name_to_nato():
    name = input("What's your name? ")
    try:
        codes = [alphabet_dict[letter.lower()] for letter in name]
    except KeyError:
        print('Letters only')
        name_to_nato()
    else:
        print(' 👏🏼 '.join(codes))
        go_again = input('Want to go again? (y/n) ')
        if go_again.lower() == 'y':
            name_to_nato()
        else:
            print('Thanks for giving this a try!')


name_to_nato()

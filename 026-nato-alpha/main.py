import pandas as pd

name = input('What is your name?')

alphabet = pd.read_csv('nato_phonetic_alphabet.csv')
alphabet_dict = {row.letter.lower(): row.code for (key, row) in alphabet.iterrows()}
codes = [alphabet_dict[letter.lower()] for letter in name]

print(codes)
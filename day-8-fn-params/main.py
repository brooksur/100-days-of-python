alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(text, shift):
    text = text.lower()
    text_list = list(text)

    for letter in text:
        letter_index = alphabet.index(letter)
        next_index = letter_index + shift
        text_list[text_list.index(letter)] = alphabet[next_index]

    return ''.join(text_list)

print(encrypt(text, shift))
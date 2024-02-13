import art

alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]


def encrypt(text, shift):
    text = text.lower()
    text_list = list(text)

    for letter in text:
        letter_index = alphabet.index(letter)
        next_index = letter_index + shift
        if next_index > 25:
            next_index = next_index - 26
        text_list[text_list.index(letter)] = alphabet[next_index]

    return ''.join(text_list)


def decrypt(text, shift):
    text = text.lower()
    text_list = list(text)

    for letter in text:
        letter_index = alphabet.index(letter)
        next_index = letter_index - shift
        if next_index < 0:
            next_index = next_index + 26
        text_list[text_list.index(letter)] = alphabet[next_index]

    return ''.join(text_list)


def cypher(original_text, shift_amount, direction):
    new_text = ""

    shift_amount = shift_amount % 26
    shift_amount = shift_amount * -1 if direction == "decode" else shift_amount

    for letter in original_text:
        if letter not in alphabet:
            new_text += letter
        else:
            next_index = alphabet.index(letter) + shift_amount

            if next_index > len(alphabet) - 1:
                next_index = alphabet.index(letter) - len(alphabet)
            elif next_index < 0:
                next_index = alphabet.index(letter) + len(alphabet)

            new_text += alphabet[next_index]

    return new_text


def run():
    dir = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    result = cypher(text, shift, dir)
    print(result)


running = True

while running:
    print(art.logo)
    run()
    if input("Do you want to continue? (y/n)\n").lower() == "n":
        print('Goodbye')
        running = False
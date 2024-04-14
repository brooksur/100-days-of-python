from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"

screen = Tk()
screen.title('Flashy ⚡')
screen.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

active_words = pandas.read_csv('data/french_words.csv')
active_words_dict = active_words.to_dict(orient='records')

try:
    words_to_learn = pandas.read_csv('data/words_to_learn.csv')
except FileNotFoundError as error:
    print(error)
else:
    active_words = words_to_learn
    active_words_dict = active_words.to_dict(orient="records")

CARD_FRONT_IMAGE = PhotoImage(file="images/card_front.png")
CARD_BACK_IMAGE = PhotoImage(file="images/card_back.png")
WRONG_BTN_IMAGE = PhotoImage(file='images/wrong.png')
RIGHT_BTN_IMAGE = PhotoImage(file='images/right.png')

flashcard = Canvas(screen, width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
flashcard_image = flashcard.create_image(400, 263, image=CARD_FRONT_IMAGE)
flashcard.grid(row=0, column=0, columnspan=2)

lang_text = flashcard.create_text(400, 150, text="French", font=('Ariel', 40, 'italic'))
word_text = flashcard.create_text(400, 253, text="Trouve", font=('Ariel', 60, 'bold'))

flip_card_active = None
word = active_words_dict[random.randint(0, len(active_words_dict))]


def new_word():
    global flip_card_active
    global word

    word = active_words_dict[random.randint(0, len(active_words_dict))]

    flashcard.itemconfig(lang_text, text='French', fill="black")
    flashcard.itemconfig(word_text, text=word['French'], fill='black')
    flashcard.itemconfig(flashcard_image, image=CARD_FRONT_IMAGE)

    def flip_card():
        flashcard.itemconfig(lang_text, text='English', fill='white')
        flashcard.itemconfig(word_text, text=word['English'], fill='white')
        flashcard.itemconfig(flashcard_image, image=CARD_BACK_IMAGE)

    if flip_card_active is not None:
        screen.after_cancel(flip_card_active)

    flip_card_active = screen.after(3000, flip_card)


def handle_right_click():
    active_words_dict.remove(word)
    pandas.DataFrame(active_words_dict).to_csv('data/words_to_learn.csv', index=False)
    new_word()


wrong_btn = Button(image=WRONG_BTN_IMAGE, highlightthickness=0, bg=BACKGROUND_COLOR, command=new_word)
right_btn = Button(image=RIGHT_BTN_IMAGE, highlightthickness=0, bg=BACKGROUND_COLOR, command=handle_right_click)

wrong_btn.grid(row=1, column=0)
right_btn.grid(row=1, column=1)

new_word()

screen.mainloop()

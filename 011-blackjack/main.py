import art
import random

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)


def calc_score(cards):
    score = sum(cards)

    if score == 21 and len(cards) == 2:
        return 0

    if score > 21 and 11 in cards:
        for card in cards:
            if card == 11 and score >= 21:
                score -= 10

    return score


def compare(user_score, dealer_score):
    if user_score == dealer_score:
        return 'Draw'
    elif user_score == 0:
        return 'User wins!'
    elif dealer_score == 0:
        return 'Dealer wins :('
    elif user_score > 21:
        return 'Dealer wins :('
    elif dealer_score > 21:
        return 'User wins!'
    elif user_score > dealer_score:
        return 'User wins!'
    else:
        return 'Dealer wins :('


def play_game():
    user_cards = [deal_card(), deal_card()]
    dealer_cards = [deal_card(), deal_card()]

    user_score = calc_score(user_cards)
    dealer_score = calc_score(dealer_cards)

    print(f"Your hand: {user_cards}\n")
    print(f"Dealer's first card: {dealer_cards[0]}\n")

    if user_score != 0 and dealer_score != 0:
        user_turn = True

        while user_turn:
            hit = input("Type 'y' to get another card, type 'n' to pass: ")
            if hit == 'y':
                user_cards.append(deal_card())
                user_score = calc_score(user_cards)
                print(f"Your cards: {user_cards}\n")
                if user_score > 21:
                    user_turn = False

            else:
                user_turn = False

        while dealer_score < 17 and user_score <= 21:
            dealer_cards.append(deal_card())
            dealer_score = calc_score(dealer_cards)

    result = compare(user_score, dealer_score)
    print(f"Your final hand: {user_cards}")
    print(f"Dealer's final hand: {dealer_cards}")
    print(result)

def run():
    print(art.logo)
    is_playing = True
    while is_playing:
        play_game()
        play_again = input("Do you want to play again? Type 'y' or 'n': \n")
        is_playing = play_again == 'y'

run()
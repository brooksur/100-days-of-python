from art import logo

bidder_list = []


def prompt_bid():
    bidder_name = input('What is your name?\n')
    bidder_amount = int(input('What is your bid?\n'))
    bidder_list.append({'name': bidder_name, 'amount': bidder_amount})


def prompt_bidders():
    more_midders = True
    while more_midders:
        prompt_bid()
        more_midders = input('Are there other bidders? (y/n)\n').lower() == 'y'


def print_winner():
    highest_bidder = {'name': '', 'amount': 0}

    for bidder in bidder_list:
        if bidder['amount'] > highest_bidder['amount']:
            highest_bidder = bidder

    print(
        f'The winner is {highest_bidder["name"]} with a bid of ${highest_bidder["amount"]}'
    )


def run():
    print(logo)
    prompt_bidders()
    print_winner()


run()

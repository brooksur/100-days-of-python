from data import MENU, resources
import re

money = 0.00


def drink_check(drink):
    for ing in drink['ingredients']:
        amount_remaining = resources[ing] - drink['ingredients'][ing]
        if amount_remaining < 0:
            return [False, ing]
    return [True]


def make_drink(drink):
    for ing in drink['ingredients']:
        resources[ing] -= drink['ingredients'][ing]


def get_report():
    return f'''
      Water: {resources['water']}ml
      Milk: {resources['milk']}ml
      Coffee: {resources['coffee']}ml
      Money: ${money}
    '''


def get_coins():
    quarters = int(input('How many quarters?'))
    dimes = int(input('How many dimes?'))
    nickels = int(input('How many nickels?'))
    pennies = int(input('How many pennies?'))

    return (quarters * .25) + (dimes * .1) + (nickels * .05) * (pennies * .01)


def handle_system_input():
    global money

    output = {
        'status': '',
        'message': '',
    }

    user_input = input('What would you like? (espresso/latte/cappuccino):')

    if user_input == 'off':
        output['status'] = 'off'
        return output

    if user_input == 'report':
        output['status'] = 'info'
        output['message'] = get_report()
        return output


    drink_regex = r"\b(espresso|latte|cappuccino)\b$"
    drink_match = bool(re.search(drink_regex, user_input))

    if drink_match:
        drink = MENU[user_input]
        check = drink_check(drink)

        if not check[0]:
            output['status'] = 'error'
            output['message'] = f'Sorry there is not enough {check[1]}'
            return output

        coins = get_coins()

        if coins < drink['cost']:
            output['status'] = 'error'
            output['message'] = f'Sorry there is not enough. Money refunded.'
        else:
            make_drink(drink)
            money = round(money + drink['cost'], 2)

            output['status'] = 'success'
            output['message'] = f'Enjoy your {user_input}'

            if coins > drink['cost']:
                print(f"You paid too much. Here is a refund ${round(coins - drink['cost'], 2)}")

    return output


running = True

while running:
    output = handle_system_input()
    print(output['message'])
    status = output['status']
    if status == 'off':
        running = False
    elif status == 'error':
        running = False
    else:
        running = True

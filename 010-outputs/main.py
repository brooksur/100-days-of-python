from art import logo

def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operations = {"+": add, "-": subtract, "*": multiply, "/": divide}

print(logo)

num1 = float(input("What's the first number?: "))

for symbol in operations:
    print(symbol)

continue_calc = True
current_result = num1

while continue_calc:
    operation_symbol = input("Pick an operation: ")
    operation = operations[operation_symbol]
    prev_result = current_result
    new_num = float(input("What number?: "))
    current_result = operation(new_num, prev_result)
    print(f"{prev_result} {operation_symbol} {new_num} = {current_result}")
    continue_calc = input('Do you want to continue? Type "y" or "n": ') == 'y'

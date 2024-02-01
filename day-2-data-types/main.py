# Data Types

# String

message = 'Hello'
# print(message)

first_char = message[0]
# print(first_char)

# Integer

int = 123
big_int = 123_456_789

# print(int)
# print(big_int)

# Float

float_ = 3.14159

# Boolean

bool = True
bool = False

street_name = "Abbey Road"
# print(street_name[4] + street_name[7])

# Conversions

chars = 'brooks' # input("What is your name? ")
print(type(chars))  # type() function -> str

num_char = len(chars)
print(type(num_char))  # type() function -> int

new_num_char = str(num_char)

print("Your name has " + new_num_char + " characters.")

a = float("123.456")
print(a)

# Mathematical Operations
print(3 + 5)
print(5 - 3)
print(3 * 2)
print(5 / 3)
print(2**6)
print(8 / 3)
print(round(8 / 3, 2))
print(8 // 3)
result = 4 / 2
result /= 2
result += 1
result *= 2
result -= 1
print('The result is ' +str(result))
result_message = f"The result is {result}"
print(result_message)

print(6 + 4 / 2 - (1 * 2))
age = input('What is your current age?')
years = 90 - int(age)
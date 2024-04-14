# try:
#     file = open('a_file.txt')
# except FileNotFoundError:
#     print('There was a file error')
#     file = open('a_file.txt', 'w')
#     file.write('Something')
# except KeyError as error_message:
#     print(f'The key {error_message} does not exist')
# else:
#     print(file.read())
# finally:
#     raise KeyError

height = float(input('Height: '))
weight = int(input('Weight: '))

if height > 3:
    raise ValueError('There are no humans 3 meters tall')


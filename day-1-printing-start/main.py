# Get the users name
name = input("What is your name?\n")

# Greet the user
print('Hello, ' + name + '! Welcome to Band Name Generator!')

# Get the users city and pet name
city = input('What\'s the name of the city you grew up in?\n')
pet = input('What\'s your pet\'s name?\n')

# Generate the band name
band_name = city + ' ' + pet

# Print the band name
print('Your band name could be ' + band_name)
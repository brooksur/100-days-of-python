# Welcome the rider
print("Welcome to the rollercoaster!")

# Get rider height
height = int(input("What is your height in cm? "))

# Check if rider is tall enough to ride
if height >= 120:
    print('You can ride the rollercoaster!')

    # Get rider age
    age = int(input("What is your age? "))

    # Check the ticket price
    if age < 12:
        print("Please pay $5.")
    elif age <= 18:
        print("Please pay $7.")
    else:
        print("Please pay $12.")

else:
    print('Sorry, you cannot ride the rollercoaster.')

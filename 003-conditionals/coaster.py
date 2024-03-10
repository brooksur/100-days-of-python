# Welcome the rider
print("Welcome to the rollercoaster!")

# Get rider height
height = int(input("What is your height in cm? "))

# Check if rider is tall enough to ride
if height >= 120:
    print('You can ride the rollercoaster!')

    # Get rider age
    age = int(input("What is your age? "))

    # Set the initial bill price
    price = 0

    if age < 12:
        price = 5
        print("Your ticket price is $5.")
    elif age <= 18:
        price = 7
        print("Your ticket price is $7.")
    elif age >= 45 and age <= 55:
        price = 0
        print("Your ticket price is $0.")
    else:
        price = 12
        print("Your ticket price is $12.")

    # Check if rider wants a photo
    wants_photo = input("Do you want a photo taken? Y or N. ")
    
    if wants_photo == "Y":
        price += 3

    # Print the final price
    print(f"Your final price is ${price}.")
else:
    print('Sorry, you cannot ride the rollercoaster.')

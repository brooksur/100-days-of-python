# Get the bill
bill = float(input("What was the total bill? $"))

# Get the tip percentage
tip = int(
    input("What percentage tip would you like to give? 10%, 12%, or 15%? "))

# Get the number of people
people = int(input("How many people to split the bill? "))

# Calculate the tip amount
tip_amount = bill * (tip / 100)

# Calculate the total bill with tip
total_bill = bill + tip_amount

# Calculate the amount each person should pay
amount_per_person = round(total_bill / people, 2)

# Print the result
print(f"Each person should pay: ${amount_per_person}")
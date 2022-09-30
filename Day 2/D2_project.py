<<<<<<< HEAD
'''
Tips: 10%, 12% or 15%
If the bill was $150.00, split between 5 people, with 12% tip.

Each person should pay (150.00 / 5) * 1.12 = 33.6

Format the result to 2 decimal places = 33.60

Thus everyone's share of the total bill is $30.00 plus a $3.60 tip.
'''
print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input('What tip are you leaving? 10%, 12% or 15%? '))
friends = int(input("How many people to split the bill? "))

bill += (bill * (tip/100))
bill_per_friend = round(bill/friends,2)

=======
'''
Tips: 10%, 12% or 15%
If the bill was $150.00, split between 5 people, with 12% tip.

Each person should pay (150.00 / 5) * 1.12 = 33.6

Format the result to 2 decimal places = 33.60

Thus everyone's share of the total bill is $30.00 plus a $3.60 tip.
'''
print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input('What tip are you leaving? 10%, 12% or 15%? '))
friends = int(input("How many people to split the bill? "))

bill += (bill * (tip/100))
bill_per_friend = round(bill/friends,2)

>>>>>>> ba2e29ddac2f6db0e1aebf50ee560d2ffe5a7d74
print(f"Each person should pay: $", bill_per_friend)
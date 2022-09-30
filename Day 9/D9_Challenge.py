import os
os.system('cls' if os.name == 'nt' else 'clear')

print("Welcome to the secret auction program")

keep = True
auction = {}

while keep:
    name = input("What is your name?: ")
    bid = int(input("What's your bid?: $"))
    decision = input("Are there others bidders?: Type 'yes' or 'no'.\n").lower()
    
    auction[name] = bid
    
    if decision == 'no':
        keep = False
    elif decision == 'yes':
        os.system('cls')
    else:
        print(("Not a valid decision!"))
        os.system('cls')

winner = ''
max_bid = 0

for i in auction:
    if auction[i] > max_bid:
        winner = i
        max_bid = auction[i]
    else:
        pass

print(f"The winner of this secret auction is: {winner}, with a bid of {max_bid}")
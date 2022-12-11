import random

logo = """
    _                        _____ _                __                 _
  / _ \_   _  ___  ___ ___  /__   \ |__   ___    /\ \ \_   _ _ __ ___ | |__   ___ _ __ 
 / /_\/ | | |/ _ \/ __/ __|   / /\/ '_ \ / _ \  /  \/ / | | | '_ ` _ \| '_ \ / _ \ '__|
/ /_\\| |_| |  __/\__ \__ \  / /  | | | |  __/ / /\  /| |_| | | | | | | |_) |  __/ |   
\____/ \__,_|\___||___/___/  \/   |_| |_|\___| \_\ \/  \__,_|_| |_| |_|_.__/ \___|_|  
"""

number = random.randint(1,100)

print(logo)
print("Welcome to the Number Guessing Game! \n I'm thinking of a number between 1 and 100")
level = input("Choose a dificulty. Type 'easy' or 'hard': ").lower()

attemps = 0
if level == 'easy':
    attemps = 10
elif level == 'hard':
    attemps = 5
else:
    print("Choose a valid dificulty!!!")

print(f"You have {attemps} attemps remaining to guess the number.")  

guess = int(input("Make a guess: "))

while(attemps):
    
    if guess == number:
        attemps = 0
        print(f"You got it! The answer was {number}")
    elif guess > number:
        attemps -= 1
        print("Too high.")
        print(f"You have {attemps} attemps remaining to guess the number.")
        guess = int(input("Make a guess: ")) 
        if attemps == 0:
            print(f"Too bad the answer was {number}")
    else:
        attemps -= 1
        print("Too low.")
        print(f"You have {attemps} attemps remaining to guess the number.")
        guess = int(input("Make a guess: "))
        if attemps == 0:
            print(f"Too bad the answer was {number}")
    
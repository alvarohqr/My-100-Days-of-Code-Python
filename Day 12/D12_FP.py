import os
os.system('cls' if os.name == 'nt' else 'clear')

import random

logo = """
    _                        _____ _                __                 _
  / _ \_   _  ___  ___ ___  /__   \ |__   ___    /\ \ \_   _ _ __ ___ | |__   ___ _ __ 
 / /_\/ | | |/ _ \/ __/ __|   / /\/ '_ \ / _ \  /  \/ / | | | '_ ` _ \| '_ \ / _ \ '__|
/ /_\\| |_| |  __/\__ \__ \  / /  | | | |  __/ / /\  /| |_| | | | | | | |_) |  __/ |   
\____/ \__,_|\___||___/___/  \/   |_| |_|\___| \_\ \/  \__,_|_| |_| |_|_.__/ \___|_|  
"""

NUMBER = random.randint(1,100)
EASY_ATTEMPS = 10
HARD_ATTEMPS = 5


def dificulty():
    level = input("Choose a dificulty. Type 'easy' or 'hard': ").lower()
    if level == 'easy':
        return EASY_ATTEMPS
    elif level == 'hard':
        return HARD_ATTEMPS
    else:
        print("Choose a valid dificulty!")
        os.system('cls')

def compare(guess, number, attemps):
    if guess > number:
        print("Too high.")
        return attemps - 1
    elif guess < number: 
        print("Too low.")
        return attemps - 1
    else:
        print(f"You got it! The answer was {NUMBER}")

def number_guesser():
    global attemps
    print(logo)
    print("Welcome to the Number Guessing Game! \n I'm thinking of a number between 1 and 100")
    attemps = dificulty()
    guess = 0
    while guess != NUMBER:
        print(f"You have {attemps} attemps remaining to guess the number.")  
        guess = int(input("Make a guess: "))
        attemps = compare(guess, NUMBER, attemps)
        if attemps == 0:
            print(f"Too bad the answer was {NUMBER}")
            return
        elif guess != NUMBER:
            print("Guess again.")
    
number_guesser()


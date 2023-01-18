from art import logo, vs
from game_data import data
import random as rnd
import os
os.system('cls' if os.name == 'nt' else 'clear') #os.system('cls')

#  Select an account from the data dictioanry

def selectGuess():
    '''
    Ramdonly returns an instagram account to compare
    '''
    account = rnd.choice(data)
    return account

def Compare(a, b):
    '''
    Checks if the two options are the same and change the later.
    '''
    cont = True
    while (cont):
        if a != b: 
            cont = False
        else: 
            b = selectGuess()
            cont  = True 
    return True
        
def Display(a, b):
    '''
    Display on the screen the two accounts to compare.
    '''
    print(logo)
    print(a['name'])
    print(vs) 
    print(b['name'])

def selectAccount(guess,a, b): 
    '''
    Returns the selected account.
    '''
    if str(guess) == str(a['name']) or str(guess) == str(a['name']).lower():
        return a
    elif str(guess) == str(b['name']) or str(guess) == str(b['name']).lower(): 
        return b
    else:
        return False
                
def displayHigher(a,b):
    '''
    Display the account whose followers account is larger.
    '''
    print(f"Correct!, {a['name']} ({a['follower_count']}M) has more followers than {b['name']} ({b['follower_count']}M).")
    print(f"{a['name']} is a {a['description']} from {a['country']} has {a['follower_count']}M followers on IG.")
    
def displayLower(a,b):
    '''
    Display the account whose followers account is larger.
    '''
    
    print(f"Wronng!, {a['name']} ({a['follower_count']}M) has less followers than {b['name']} ({b['follower_count']}M).")
    print(f"{b['name']} is a {b['description']} from {b['country']} has {b['follower_count']}M followers on IG.")

def Game(a, b):
    '''
    Guess the account who has more followers on Instagram.
    '''
    Display(a, b)
    
    cont = 'Y'
    # Infinite loop
    while(1):
        
        # Checking if the accounts are not the same
        Compare(a, b)
        # Guessing the account with more followers
        guess = input("Who has more followers: ")
        #selectAccount(guess, a, b)
        answer = selectAccount(guess, a, b)
        if (answer):
            # 1st account has more followers
            if int(answer['follower_count']) > int(b['follower_count']):
                displayHigher(a, b)
                # The first acount is right so refresh the second.
                b = selectGuess()
            # 2nd account has more followers
            else:
                displayLower(a, b)
                # swaping the accounts, so the last right option displays first: Last vs New
                a, b = b, selectGuess() 
        else:
            print("Enter a valid option!!!")   
        cont = input("Continue playing? ")
        if (cont == 'Y' or cont == 'y'):
            # Recursive Call
            Game(a, b)
        
        os.system('cls')
        break
        

a = selectGuess()
b = selectGuess()   
# print(a['name'])
# print(b['name'])
# guess = input("Who has more followers: ")
# print(selectAccount(guess, a, b))
Game(a, b)
import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

def chooses(a):
    if a == 0:
        print(rock)
    elif a == 1:
        print(paper)
    elif a == 2:
        print(scissors)
    else:
        print("Type a valid option!")

choose = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
chooses(choose)
 
computer_choose = random.randint(0,2)
print("Computer choose: ")
chooses(computer_choose)

'''
Lose:
    0 - 1 = -1
    1 - 2 = -1
    2 - 0 = 2
Win:
    0 - 2 = -2
    1 - 0 = 1
    2 - 1 = 1
'''

if choose == computer_choose: 
    print("It's a draw")
    # 1 - 2 = -1
elif choose - computer_choose == -1 or choose - computer_choose ==2:
    print("You lose") 
elif choose - computer_choose == 1 or choose - computer_choose ==-2:
    print("You win")
else:
    print("Not yet")



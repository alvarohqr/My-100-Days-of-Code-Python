'''
wea = 'WEAS LOCAS'

print(wea.index('L'))

weas = ''

for i in wea:
    weas += ' _'


print(weas)
'''

import random

#Step 1 

word_list = ["aardvark", "baboon", "camel"]

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.

#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.

#TODO 1
chosen_word = word_list[random.randint(0,len(word_list)-1)]

#chosem_word = random.choise(word_list)

#TODO 2
guess = input("Gues a letter: ").lower()

#TODO 3
for i in range(len(chosen_word)):
    if chosen_word[i] == guess:
        print("Right")
    else:
        print("Wrong")

'''
for i in chosen_word:
    if i == guess:
        print("Right")
    else:
        print("Wrong")
'''
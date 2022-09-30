#Step 2

from dis import dis
import random
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#TODO-1: - Create an empty List called display.
#For each letter in the chosen_word, add a "_" to 'display'.
#So if the chosen_word was "apple", display should be ["_", "_", "_", "_", "_"] with 5 "_" representing each letter to guess.

display = []

for i in chosen_word:
    display.append("_")

lives = 6
 
end_game = False
#TODO-1: - Use a while loop to let the user guess again. The loop should only stop once the user has guessed all the letters in the chosen_word and 'display' has no more blanks ("_"). Then you can tell the user they've won.


#Check guessed letter
while not end_game :
    guess = input("Guess a letter: ").lower()
    for position in range(word_length):
        letter = chosen_word[position] 
        if letter == guess:
            display[position] = letter
        
    print(display)

    if "_" not in display:
        print("You Won")
        end_game: True
        
    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            end_game = True
            print("You lose.")
    


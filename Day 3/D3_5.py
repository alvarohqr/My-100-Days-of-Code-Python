'''
You are going to write a program that tests the compatibility between two people.
To work out the love score between two people:
Take both people's names and check for the number of times the letters in the word TRUE occurs. 
Then check for the number of times the letters in the word LOVE occurs. 
Then combine these numbers to make a 2 digit number.
For Love Scores less than 10 or greater than 90, the message should be:
"Your score is **x**, you go together like coke and mentos."
For Love Scores between 40 and 50, the message should be:
"Your score is **y**, you are alright together."
Otherwise, the message will just be their score. e.g.:
"Your score is **z**."
'''

# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

names = (name1 + ' ' + name2).upper()

true_count = 0 #TRUE counter 
love_count = 0 #LOVE counter 
for i in names:
    if i == 'T' or i == 'R' or i == 'U' or i == 'E':
        true_count += 1
    if i == 'L' or i == 'O' or i == 'V' or i == 'E':
        love_count += 1

love_score = str(true_count)+str(love_count)
score = int(love_score)

if score < 10 or score > 90:
    print(f"Your score is {love_score}, you go together like coke and mentos.")
elif score > 40 and score < 50:
    print(f"Your score is {love_score}, you are alright together.")
else:
     print(f"Your score is {love_score}.")





    
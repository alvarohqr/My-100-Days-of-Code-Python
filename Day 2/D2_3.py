<<<<<<< HEAD
'''
Create a program using maths and f-Strings that tells us how many days,
weeks, months we have left if we live until 90 years old.
It will take your current age as the input and output a message with our time left in this format:
You have x days, y weeks, and z months left.
Where x, y and z are replaced with the actual calculated numbers.
'''

# 🚨 Don't change the code below 👇
age = input("What is your current age? 26")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

years_left = 90 - int(age)
days = years_left * 365
weeks = years_left * 52
months = years_left * 12

=======
'''
Create a program using maths and f-Strings that tells us how many days,
weeks, months we have left if we live until 90 years old.
It will take your current age as the input and output a message with our time left in this format:
You have x days, y weeks, and z months left.
Where x, y and z are replaced with the actual calculated numbers.
'''

# 🚨 Don't change the code below 👇
age = input("What is your current age? 26")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

years_left = 90 - int(age)
days = years_left * 365
weeks = years_left * 52
months = years_left * 12

>>>>>>> ba2e29ddac2f6db0e1aebf50ee560d2ffe5a7d74
print(f"You have {days} days, {weeks} weeks, and {months} months left.") #F-String, {variable}
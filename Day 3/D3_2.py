<<<<<<< HEAD
''' 
Write a program that interprets the Body Mass Index (BMI) based on a user's weight and height.
It should tell them the interpretation of their BMI based on the BMI value.
    Under 18.5 they are underweight
    Over 18.5 but below 25 they have a normal weight
    Over 25 but below 30 they are slightly overweight
    Over 30 but below 35 they are obese
    Above 35 they are clinically obese.
'''

# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

BMI = round((weight / (height**2)))

if BMI < 18.5:
    print(f"Your BMI is {BMI}, you are underweight.")
elif BMI > 18.5 and BMI < 25:
    print(f"Your BMI is {BMI}, you have a normal weight.")
elif BMI > 25 and BMI < 30:
    print(f"Your BMI is {BMI}, you are slightly overweight.")
elif BMI > 30 and BMI < 35:
    print(f"Your BMI is {BMI}, you are obese.")
elif BMI > 35:
=======
''' 
Write a program that interprets the Body Mass Index (BMI) based on a user's weight and height.
It should tell them the interpretation of their BMI based on the BMI value.
    Under 18.5 they are underweight
    Over 18.5 but below 25 they have a normal weight
    Over 25 but below 30 they are slightly overweight
    Over 30 but below 35 they are obese
    Above 35 they are clinically obese.
'''

# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

BMI = round((weight / (height**2)))

if BMI < 18.5:
    print(f"Your BMI is {BMI}, you are underweight.")
elif BMI > 18.5 and BMI < 25:
    print(f"Your BMI is {BMI}, you have a normal weight.")
elif BMI > 25 and BMI < 30:
    print(f"Your BMI is {BMI}, you are slightly overweight.")
elif BMI > 30 and BMI < 35:
    print(f"Your BMI is {BMI}, you are obese.")
elif BMI > 35:
>>>>>>> ba2e29ddac2f6db0e1aebf50ee560d2ffe5a7d74
    print(f"Your BMI is {BMI}, you are clinically obese.")
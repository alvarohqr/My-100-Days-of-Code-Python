<<<<<<< HEAD
'''
Write a program that calculates the Body Mass Index (BMI) from a user's weight and height.

The BMI is a measure of some's weight taking into account their height. 
e.g. If a tall person and a short person both weigh the same amount, 
the short person is usually more overweight.

The BMI is calculated by dividing a person's weight (in kg) by the square of their height (in m):
'''

# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
BMI = float(weight)/pow(float(height),2)
=======
'''
Write a program that calculates the Body Mass Index (BMI) from a user's weight and height.

The BMI is a measure of some's weight taking into account their height. 
e.g. If a tall person and a short person both weigh the same amount, 
the short person is usually more overweight.

The BMI is calculated by dividing a person's weight (in kg) by the square of their height (in m):
'''

# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
BMI = float(weight)/pow(float(height),2)
>>>>>>> ba2e29ddac2f6db0e1aebf50ee560d2ffe5a7d74
print(int(BMI))
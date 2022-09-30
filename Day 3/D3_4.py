<<<<<<< HEAD
'''
Congratulations, you've got a job at Python Pizza. 
Your first job is to build an automatic pizza order program.
Based on a user's order, work out their final bill.
Small Pizza: $15
Medium Pizza: $20
Large Pizza: $25
Pepperoni for Small Pizza: +$2
Pepperoni for Medium or Large Pizza: +$3
Extra cheese for any size pizza: + $1
'''
# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
if size == 'S' and add_pepperoni == 'Y':
    bill = 15 + 2
if size == 'S' and add_pepperoni == 'N':
    bill = 15
if size == 'M' and add_pepperoni == 'Y':
    bill = 20 + 3
if size == 'M' and add_pepperoni == 'N':
    bill = 20 
if size == 'L' and add_pepperoni == 'Y':
    bill = 25 +3
if size == 'L' and add_pepperoni == 'N':
    bill = 25 
if extra_cheese == 'Y':
    bill += 1
if extra_cheese == 'N':
    bill = bill

=======
'''
Congratulations, you've got a job at Python Pizza. 
Your first job is to build an automatic pizza order program.
Based on a user's order, work out their final bill.
Small Pizza: $15
Medium Pizza: $20
Large Pizza: $25
Pepperoni for Small Pizza: +$2
Pepperoni for Medium or Large Pizza: +$3
Extra cheese for any size pizza: + $1
'''
# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
if size == 'S' and add_pepperoni == 'Y':
    bill = 15 + 2
if size == 'S' and add_pepperoni == 'N':
    bill = 15
if size == 'M' and add_pepperoni == 'Y':
    bill = 20 + 3
if size == 'M' and add_pepperoni == 'N':
    bill = 20 
if size == 'L' and add_pepperoni == 'Y':
    bill = 25 +3
if size == 'L' and add_pepperoni == 'N':
    bill = 25 
if extra_cheese == 'Y':
    bill += 1
if extra_cheese == 'N':
    bill = bill

>>>>>>> ba2e29ddac2f6db0e1aebf50ee560d2ffe5a7d74
print(f"Your final bill is: ${bill}.")
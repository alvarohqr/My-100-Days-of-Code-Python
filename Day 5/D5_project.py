<<<<<<< HEAD
#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

order_letters = ''
order_numbers = ''
order_symbols = ''

for i in range(0,nr_letters):
#for i in range(1, nr_letters + 1):    
    order_letters += letters[random.randint(0,len(letters)-1)]
    #order_letters += random.choice(letters)
    
for j in range(0,nr_symbols):
    order_symbols += symbols[random.randint(0,len(symbols)-1)]
    
for k in range(0,nr_numbers):
    order_numbers += numbers[random.randint(0,len(numbers)-1)]

easy_password = order_letters+order_symbols+order_numbers

print(f"Easy level password: {easy_password}")

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

hard = sorted(easy_password)

hard_password = ''

for l in range(0, len(hard)-1):
    hard_password += hard[random.randint(0, len(hard)-1)]
    
=======
#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

order_letters = ''
order_numbers = ''
order_symbols = ''

for i in range(0,nr_letters):
#for i in range(1, nr_letters + 1):    
    order_letters += letters[random.randint(0,len(letters)-1)]
    #order_letters += random.choice(letters)
    
for j in range(0,nr_symbols):
    order_symbols += symbols[random.randint(0,len(symbols)-1)]
    
for k in range(0,nr_numbers):
    order_numbers += numbers[random.randint(0,len(numbers)-1)]

easy_password = order_letters+order_symbols+order_numbers

print(f"Easy level password: {easy_password}")

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

hard = sorted(easy_password)

hard_password = ''

for l in range(0, len(hard)-1):
    hard_password += hard[random.randint(0, len(hard)-1)]
    
>>>>>>> ba2e29ddac2f6db0e1aebf50ee560d2ffe5a7d74
print(f"Hard level passoword: {hard_password}")
<<<<<<< HEAD
#Remember to use the random module
#Hint: Remember to import the random module here at the top of the file. 🎲

import random 

# 🚨 Don't change the code below 👇
test_seed = int(input("Create a seed number: "))
random.seed(test_seed)
 # 🚨 Don't change the code above 👆 It's only for testing your code.
	 
#Write the rest of your code below this line 👇
coin = random.randint(-0,1)

if coin == 0:
    print("Tails")
elif coin == 1:
    print("Heads")
else:
    print("Something went wrong")
=======
#Remember to use the random module
#Hint: Remember to import the random module here at the top of the file. 🎲

import random 

# 🚨 Don't change the code below 👇
test_seed = int(input("Create a seed number: "))
random.seed(test_seed)
 # 🚨 Don't change the code above 👆 It's only for testing your code.
	 
#Write the rest of your code below this line 👇
coin = random.randint(-0,1)

if coin == 0:
    print("Tails")
elif coin == 1:
    print("Heads")
else:
    print("Something went wrong")
>>>>>>> ba2e29ddac2f6db0e1aebf50ee560d2ffe5a7d74

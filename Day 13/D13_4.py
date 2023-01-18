############DEBUGGING#####################

# Fix the Errors
#age = input("How old are you? ") 
age = int(input("How old are you? "))
# in this case, age wich is a str is being compared to a int
if age >= 18:
    #print("You can drive at age {age}.")
    #also the print staments is not in f format, so:
    print(f"You can drive at age {age}.")
#if you're underage the program does nothing, so:
elif age < 18:
    print(f"You can't drive at age {age}.")
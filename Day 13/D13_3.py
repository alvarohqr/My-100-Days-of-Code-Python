############DEBUGGING#####################

# Play Computer
year = int(input("What's your year of birth? "))
if year > 1980 and year < 1994:
   print("You are a millenial.")
#elif year > 1994:
# if you were before 1980 or in 1994 the code does nothing, so:
elif year >= 1994:
   print("You are a Gen Z.")
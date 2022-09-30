'''
Instructions at:
https://app.diagrams.net/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#G1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi

'You're at a crossroad. Where do you want to go? Type "left" or "right"'
'You've come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across.'
"You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?"
"It's a room full of fire. Game Over."
"You found the treasure! You Win!"
"You enter a room of beasts. Game Over."
"You chose a door that doesn't exist. Game Over."
"You get attacked by an angry trout. Game Over."
"You fell into a hole. Game Over."

'''

print('''
      *******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/____/[ElAlvaro]
*******************************************************************************
      ''')

'''
'You're at a crossroad. Where do you want to go? Type "left" or "right"'
'You've come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across.'
"You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?"
"It's a room full of fire. Game Over."
"You found the treasure! You Win!"
"You enter a room of beasts. Game Over."
"You chose a door that doesn't exist. Game Over."
"You get attacked by an angry trout. Game Over."
"You fell into a hole. Game Over."
'''
start = input("You're at a crossroad. Where do you want to go? Type 'left' or 'right' ")

if start.lower() == 'left':
    lake = input("You've come to a lake. There is an island in the middle of the lake. Type 'wait' to wait for a boat. Type 'swim' to swim across. ")
else:
    print("You've fell into a hole\n Game Over!")
if lake.lower() == 'wait':
    door = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose? ")
else:
    print("You were attacked by trout\n Game Over!")
if door.lower() == 'red':
    print("Burned by fire\n Game Over!")
elif door.lower() == 'blue':
    print("Eaten by beast\n Game Over!")
elif door.lower() == 'yellow':
    print("You Win!")
else:
    print("Game Over!")
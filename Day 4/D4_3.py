# 🚨 Don't change the code below 👇
row1 = ["⬜️","️⬜️","️⬜️"]
row2 = ["⬜️","⬜️","️⬜️"]
row3 = ["⬜️️","⬜️️","⬜️️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
coords = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

#Write your code below this row 👇

i = int(coords[0]) - 1
j = int(coords[1]) - 1
#Es como una matriz transpuesta 
map[j][i] = 'X'

for xy in map:
    print(xy)

#Write your code above this row 👆

# 🚨 Don't change the code below 👇
#print(f"{row1}\n{row2}\n{row3}")


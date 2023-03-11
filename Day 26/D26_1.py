# Add 1 to all list members
numbers = [1, 2, 3]
my_name = "Alvaro"

# Basic way 
'''
new_list = []
for n in numbers:
    add_1 = n + 1
    new_list.append(add_1)

print(new_list)
'''

#List comprehension
# new_list = [new_item for item in list]
# new_list = [new_item for item in list if item test]

new_list = [n +1 for n in numbers]
print(*new_list)
#----------------------------------------
letter_list = [letter for letter in my_name]
print(*letter_list)
#----------------------------------------
range_list = [n * 2 for n in range(1, 5)]
print(*range_list)
#----------------------------------------
names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Fredie"]
short_names = [name for name in names if len(name) < 5]
print(*short_names)

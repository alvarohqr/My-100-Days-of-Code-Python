'''
You are going to write a program that calculates the highest score from a List of scores
Important you are not allowed to use the max or min functions. The output words must match the example. i.e
The highest score in the class is: x
'''

# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆

#Write your code below this row 👇

max_value = 0

for i in student_scores:
    if i >= max_value:
        max_value = i
    else:
        max_value = max_value

print(f"The highest score in the class is: {max_value}")



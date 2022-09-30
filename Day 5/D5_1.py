<<<<<<< HEAD
# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇
count = 0
suma = 0

for i in student_heights:
    count += 1 
    suma += i


=======
# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇
count = 0
suma = 0

for i in student_heights:
    count += 1 
    suma += i


>>>>>>> ba2e29ddac2f6db0e1aebf50ee560d2ffe5a7d74
print(round(suma/count))
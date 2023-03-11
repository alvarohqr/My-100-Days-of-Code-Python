# Dictionary comprehension
#new_dictionary = {new_key: new_value for (key, value) in dict.items() if test}
#new_dictionary = {new_key: new_value for item in list}

import random
names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Fredie"]
studen_scores = {student: random.randint(1,100) for student in names}

pased_students = {student: score for (student, score) in studen_scores.items() if score >= 60}
print(*pased_students)
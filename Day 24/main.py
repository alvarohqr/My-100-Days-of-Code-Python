# Read File

# with open("C:/Users/alvar/OneDrive/Documentos/CURSOS/100 Days of Code The Complete Python Pro Bootcamp for 2022/Day 24/my_file.txt") as file:
#     contents = file.read()
#     print(contents) 

# Rewrite File
with open("C:/Users/alvar/OneDrive/Documentos/CURSOS/100 Days of Code The Complete Python Pro Bootcamp for 2022/Day 24/my_file.txt", "w") as file:
    file.write("Donkey Donuts to you my friend")
    
# Write File
with open("C:/Users/alvar/OneDrive/Documentos/CURSOS/100 Days of Code The Complete Python Pro Bootcamp for 2022/Day 24/my_file.txt", "a") as file:
    file.write("\nGame Pass a 10 pesos")

# New File
with open("C:/Users/alvar/OneDrive/Documentos/CURSOS/100 Days of Code The Complete Python Pro Bootcamp for 2022/Day 24/my_new_file.txt", "w") as file:
    file.write("Pizzas")
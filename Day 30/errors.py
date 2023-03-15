# try:
#     file = open("a_file.txt")
#     a_dictionary = {"key": "value"}
#     print(a_dictionary["key"])
# except FileNotFoundError: 
#     file = open("Day 30/a_file.txt", "a")
#     file.write("\nSomething")
# except KeyError as error_message: 
#     print(f"Thay key {error_message} does not exist.")
# else:
#     content = file.read()
#     print(content)
# finally:
#     # file.close()
#     # print("File was closed.")
#     raise KeyboardInterrupt("YO")

height = float(input("Height: "))
weight = int(input("Weight: "))

if height > 3:
    raise TypeError("Human height should not be over 3 meters")

bmi = weight / height ** 2
print(f"{bmi}")
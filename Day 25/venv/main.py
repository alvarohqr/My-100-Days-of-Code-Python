# with open("Day 25/venv/weather_data.csv") as data:
#     contents = data.readlines()

# print(contents)

import pandas as pd

# import csv
# with open("Day 25/venv/weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != 'temp':
#             temperatures.append(int(row[1]))
#     print(temperatures)
    
# data = pd.read_csv("Day 25/venv/weather_data.csv")
# print(type(data))
# print(type(data["temp"]))

# data_dict = data.to_dict()
# print(data_dict)

#data['temp'] = data.temp

# temp_list = data["temp"].to_list()
# print(f"Average temperature: {sum(temp_list)/len(temp_list)}")
# print(f"Average temperature with pandas: {data['temp'].mean()}")
# print(F"Max temperature: {data['temp'].max()}")

# # print("LATEX")
# # data_tex = data["temp"].to_latex()
# # print(data_temp)

#Get data from Monday
#print(data[data.temp == "Monday"])

#Get data from the day with max temperature
# print(data[data.temp == data.temp.max()])

# monday = data[data.day == "Monday"]
# monday_tempF= (1.8 * int(monday.temp)) + 32
# print(f"Temperature on monday (°F): {monday_tempF}")

#Create a dataframe from scratch
data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 100]
}

data = pd.DataFrame(data=data_dict)
data.to_csv("Day 25/venv/pandas.csv")
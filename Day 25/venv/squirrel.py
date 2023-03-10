import pandas as pd

data = pd.read_csv("Day 25/venv/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

color = data["Primary Fur Color"]

countGray = 0
countCinnamon = 0
countBlack = 0

# iterate trough the color series and increase the color count
for primary_color in color:
    if primary_color == "Gray":
        countGray += 1
    elif primary_color == "Cinnamon":
        countCinnamon += 1
    elif primary_color == "Black":
        countBlack += 1

# session solution
gray_squirrels = len(color[data["Primary Fur Color"] == "Gray"])
cinnamon_squirrels = len(color[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels = len(color[data["Primary Fur Color"] == "Black"])

print(f"Gray: {countGray}, Black: {countBlack}, Cinnamon: {countCinnamon}")
print(f"Session solution:\nGray: {gray_squirrels}, Black: {black_squirrels}, Cinnamon: {cinnamon_squirrels}")

#hold the data into a dictionary
squirrel_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [countGray, countCinnamon, countBlack]
}

#convert the dictionary into a pandas dataframe and saving it in a csv
squirrel_csv = pd.DataFrame(squirrel_dict)
squirrel_csv.to_csv("Day 25/venv/squirrel_count.csv")
        
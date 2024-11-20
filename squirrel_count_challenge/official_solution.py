# 100 Days of Code: The Complete Python Pro Bootcamp by Dr. Angela Yu
# Day 25 - Intermediate - Working with CSV Data and the Pandas Library
# Central Park Squirrel Data Analysis
# Challenge - Count the number of squirrels of each color from CSV file and save results to a new CSV file
# Official solution

import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20241107.csv")
grey_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])
print(grey_squirrels_count)
print(red_squirrels_count)
print(black_squirrels_count)

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [grey_squirrels_count, red_squirrels_count, black_squirrels_count]
}

df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_count_2.csv")
# 100 Days of Code: The Complete Python Pro Bootcamp by Dr. Angela Yu
# Day 25 - Intermediate - Working with CSV Data and the Pandas Library
# Challenge - Count the number of squirrels of each color from CSV file and save results to a new CSV file

# Data is From 2018 Central Park Squirrel Census - Squirrel Data
# https://data.cityofnewyork.us/Environment/2018-Central-Park-Squirrel-Census-Squirrel-Data/vfnx-vebw/about_data
# https://www.thesquirrelcensus.com/

import pandas

# Get data from CSV
squirrels_data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20241107.csv")
# Count number of squirrels of each color
squirrels_count_gray = squirrels_data['Primary Fur Color'].value_counts()['Gray']
squirrels_count_black = squirrels_data['Primary Fur Color'].value_counts()['Black']
squirrels_count_red = squirrels_data['Primary Fur Color'].value_counts()['Cinnamon']
print(f"There are {squirrels_count_gray} gray squirrels, {squirrels_count_black} black squirrels and {squirrels_count_red} red squirrels.")
# Convert count data to a dictionary
squirrel_count = {
    "Fur Color": ["gray", "black", "red"],
    "Count": [squirrels_count_gray, squirrels_count_black, squirrels_count_red]
}
print(squirrel_count)
# Convert dictionary data to pandas data frame object
squirrel_count_pd = pandas.DataFrame(squirrel_count)
# Save the data count to CSV file
squirrel_count_pd.to_csv("squirrel_count.csv")
# 100 Days of Code: The Complete Python Pro Bootcamp by Dr. Angela Yu
# Day 25 - Intermediate - Working with CSV Data and the Pandas Library

# import csv

# with open("weather_data.csv") as weather_data:
#     data = weather_data.readlines() # Turn each data line into a separate list item
# print(data)

# with open("weather_data.csv") as weather_data:
#     data = csv.reader(weather_data)
#     # Challenge create a list with temperature data
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)

import pandas

# data = pandas.read_csv("weather_data.csv") # much less lines than csv module
# print(data)
# print(data["temp"]) # to print temp column, much quicker
# print(type(data)) # DataFrame - 2D, for rows and columns type of data
# print(type(data["temp"])) # Series - 1D, similar to a list

# data_dict = data.to_dict() # convert Pandas data object to a dictionary
# print(data_dict)
#
# temp_list = data["temp"].to_list() # convert Series data object to a list
# print(temp_list)
# print(type(temp_list))
#
# temp_avg = data["temp"].mean()
# print(temp_avg)
#
# temp_max = data["temp"].max()
# print(temp_max)
#
# # Get data in columns
# print(data["condition"]) # case sensitive
# # or:
# print(data.condition)

# # Get data in row
# print(data[data.day == "Monday"]) # where day is the 1st column, and Monday is the row that'll be pulled

# # Challenge - print the row of data which had the highest temperature
# max_temp = data.temp.max() # or data["temp"].max()
# max_temp_row = data[data.temp == max_temp]
# print(max_temp_row)
#



# # Challenge - convert Monday's temperature to Fahrenheit. Hint use [] to get a single value from the pandas Series by index
# monday = data[data.day == "Monday"]
# # print(monday.condition) # Get condition on a specific day
# # monday_dict = monday.to_dict()
# # monday_temp_c = monday_dict["temp"][0]
# # monday_temp_f = (monday_temp_c * 1.8) + 32
# # or (official solution)
# monday_temp = monday.temp[0]
# monday_temp_f = (monday_temp * 1.8) + 32
# print(type(monday_temp)) # <class 'numpy.int64'>
# print(f"Monday's temperature is {monday_temp}ºC or {monday_temp_f}ºF.")

# # Create a dataframe from scratch and save it as CSV file
# data2_dict = {
#     "student": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }
# data2 = pandas.DataFrame(data2_dict)
# data2.to_csv("new_data.csv")
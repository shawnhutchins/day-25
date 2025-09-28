#with open("weather_data.csv") as data_file:
#    data = data_file.readlines()
#   for index in range(len(data)):
#        data[index] = data[index].strip("\n")

# import csv
#
# TEMP_COL = 1
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     #skipping the first row of the data
#     next(data)
#     for row in data:
#         temperatures.append(int(row[TEMP_COL]))
#     print(temperatures)

import pandas

data = pandas.read_csv("weather_data.csv")
temperatures = data["temp"]
#print(type(data))
#print(type(temperatures))

data_dict = data.to_dict()
#print(data_dict)

temps_list = temperatures.to_list()

print(data["temp"].mean())
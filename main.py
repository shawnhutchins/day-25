#with open("weather_data.csv") as data_file:
#    data = data_file.readlines()
#   for index in range(len(data)):
#        data[index] = data[index].strip("\n")

import csv

TEMP_COL = 1

with open("weather_data.csv") as data_file:
    data = csv.reader(data_file)
    temperatures = []
    next(data)
    for row in data:
        temperatures.append(int(row[TEMP_COL]))
    print(temperatures)
with open("weather_data.csv") as data_file:
    data = data_file.readlines()
    for index in range(len(data)):
        data[index] = data[index].strip("\n")

print(data)
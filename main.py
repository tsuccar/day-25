####################
#  Solution #1
# import csv
# with open("weather_data.csv", "r") as data_file:
#     data = csv.reader(data_file)
#     listed = list(data)
#     temperature = []
#     for row in listed[1:]:
#         temperature.append(int(row[1]))
# print(temperature)

####################
#  Solution #2
####################
# import csv
#
# with open("weather_data.csv", "r") as data_file:
#     data = csv.reader(data_file)
#     listed_data = []
#     temperature = []
#     for data_row in data:
#         listed_data.append(data_row)
#     for listed_row in listed_data[1:]:
#         temperature.append(int(listed_row[1]))
# print(temperature)

####################
#  Solution #3
####################

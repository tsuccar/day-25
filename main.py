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
# print(listed)
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
# print(listed_data)
####################
#  Solution #3
####################
# import pandas as pd
# data = pd.read_csv("weather_data.csv")
# temperature1 = data["temp"]
# print(type(temperature1))
# temperature2 = data["temp"].tolist()
# print(type(temperature2))
# print(temperature2)
# print(data)
# avg_temp = sum(temperature2)/len(temperature2)
# print(avg_temp)
# avg_temp2=data["temp"].mean()
# print(avg_temp2)
# max_value=data['temp'].max()
# print(f"maximum value {max_value}")
#
# # Show Maximum Temperature Row
# max_temp_row = data[data.temp == data['temp'].max()]
# print(max_temp_row)
#
# # Convert Monday's temperature to Farheneight
# monday = data [data.day == "Monday"]
# print (1.8*monday.temp+32)

############ Solution 1 - not quite- row number is scewed###############
# import pandas as pd
# cpark_data = pd.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')
# fur_color_column = cpark_data["Primary Fur Color"]
# freq_dic = {}
# for item in fur_color_column :
# 	if item in freq_dic:
# 		freq_dic[item] += 1
# 	else:
# 		freq_dic[item] = 1
# sqrlcount_pd_frame = pd.DataFrame()
# sqrlcount_pd_frame["Fur Color"] = list(freq_dic.keys())
# sqrlcount_pd_frame["Count"] = list(freq_dic.values())
# sqrlcount_pd_frame = sqrlcount_pd_frame[1:]
# sqrlcount_pd_frame.to_csv("squirrel_count.csv")

############ Solution 2 - Correct Answer ###############
# import pandas as pd
# cpark_data = pd.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')
# fur_color_column = cpark_data["Primary Fur Color"]
# squirrel_count= pd.DataFrame()
# squirrel_count["fur color"] = fur_color_column[fur_color_column.notnull()].unique()
#
# selected_Cinnamon_row = cpark_data[cpark_data["Primary Fur Color"] =="Cinnamon"]
# total_Cinnamon = selected_Cinnamon_row["Primary Fur Color"].count()
# selected_Gray_row = cpark_data[cpark_data["Primary Fur Color"] =="Gray"]
# total_Gray = selected_Gray_row["Primary Fur Color"].count()
# selected_Black_row = cpark_data[cpark_data["Primary Fur Color"] =="Black"]
# total_Black = selected_Black_row["Primary Fur Color"].count()
# squirrel_count["count"] = [total_Gray,total_Cinnamon,total_Black]
# squirrel_count.to_csv('squirrel_count.csv')

############ Solution 3 - not exact solution ###############
# import pandas as pd
# cpark_data = pd.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')
# fur_color_column = cpark_data["Primary Fur Color"].value_counts()
# fur_color_column.to_csv("squirrel_count.csv")


########### Solution 4 - from class #####3

import pandas as pd
cpark_data = pd.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')
fur_color_column = cpark_data["Primary Fur Color"]

selected_Cinnamon_row = cpark_data[cpark_data["Primary Fur Color"] =="Cinnamon"]
total_Cinnamon = selected_Cinnamon_row["Primary Fur Color"].count()
selected_Gray_row = cpark_data[cpark_data["Primary Fur Color"] =="Gray"]
total_Gray = selected_Gray_row["Primary Fur Color"].count()
selected_Black_row = cpark_data[cpark_data["Primary Fur Color"] =="Black"]
total_Black = selected_Black_row["Primary Fur Color"].count()

sqrl_dict = {
	"Fur Color" : ["Gry", "Cinnamon", "Black"],
	"Count" : [total_Gray,total_Cinnamon,total_Black]
}

squirrel_count = pd.DataFrame(sqrl_dict)
squirrel_count.to_csv('squirrel_count.csv')

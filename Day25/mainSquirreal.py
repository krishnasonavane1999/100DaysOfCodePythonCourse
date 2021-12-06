# # reading CSV data from the file
# # with open("weather_data.csv", "r") as file:
# # 	data = file.readlines()
# # 	# data = data.split(',')
# # 	print(data)

# # import csv
# # with open("weather_data.csv", "r") as data_file:
# # 	data = csv.reader(data_file)
# # 	temperatures = []
# # 	for row in data:
# # 		if row[1] != "temp":
# # 			str_to_int = int(row[1])
# # 			temperatures.append(str_to_int)
# # 		else:
# # 			pass

# # 	print(temperatures)



# import pandas

# data = pandas.read_csv("weather_data.csv")
# # print(data["temp"])

# # data_dict = data["temp"].to_list()

# # avg_temp = sum(data_dict) / len(data_dict)

# # print("Avg temp: ", (avg_temp))
# # print(data["temp"].mean())
# # print(data["temp"].max())

# # print(data[data.temp == data.temp.max()])

# data_dict = {
# 	"students": ["krishna", "Paras", "chandler"],
# 	"scores": [1, 2, 3]

# }

# data = pandas.DataFrame(data_dict)
# print(data)

# data.to_csv("newData.csv")



import pandas

data = pandas.read_csv("squirrel_data_2018.csv")

gray_squirreal = len(data[data["Primary Fur Color"] == "Gray"])
cinnamon_squirreal = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirreal = len(data[data["Primary Fur Color"] == "Black"])

print(gray_squirreal)
print(cinnamon_squirreal)
print(black_squirreal)

data_dict = {
	
	"Fur color": ["Gray", "Cinnamon", "Black"],
	"Count": [gray_squirreal, cinnamon_squirreal, black_squirreal]
}

data_frame = pandas.DataFrame(data_dict)

data_frame.to_csv("SquirrelData.csv")
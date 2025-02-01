# with open("weather_data.csv", "r") as data_file:
#     data = data_file.readlines()
#     print(data)

# import csv
#
# with open("weather_data.csv", "r") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)

import pandas

# data = pandas.read_csv("weather_data.csv")
# print(data["temp"])

# data_dict = data.to_dict()
# print(data_dict)
#
# temp_list = data["temp"].to_list()
#
# average = data['temp'].mean()
# print(f"Average: {average}")
#
# max_value = data['temp'].max()
# print(f"Maximum Value: {max_value}")
#
# # Get data in columns
# print(data["condition"])

# # Get data in rows
# print(data[data.day == "Monday"])

# print(data[data.temp == data["temp"].max()])

# monday = data[data.day == "Monday"]
# monday_temp = monday.temp
# monday_temp_F = monday_temp * 9/5 +32
# print(monday_temp_F)

# Create a dataframe from scratch
data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}
student_data= pandas.DataFrame(data_dict)
student_data.to_csv("new_data.csv")
print(student_data)
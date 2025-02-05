import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

gray_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])

cinnamon_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])

black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])

data_dict = {
    "Fur color": ["Grey", "Cinnamon", "Black"],
    "Count": [gray_squirrels_count, cinnamon_squirrels_count, black_squirrels_count]
}

squirrel_data = pandas.DataFrame(data_dict)
squirrel_data.to_csv("squirrel_count.csv")
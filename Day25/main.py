import pandas

data = pandas.read_csv("squirrel.csv")
gray_squirreles_count = len(data[data["Primary Fur Color"] == "Gray"])
black_squirreles_count = len(data[data["Primary Fur Color"] == "Black"])
red_squirreles_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
print(gray_squirreles_count)
print(black_squirreles_count)
print(red_squirreles_count)

data_dict = {
    "Color": ["Grey" , "Black", "Red"],
    "Count": [gray_squirreles_count, black_squirreles_count, red_squirreles_count]
}

df = pandas.DataFrame(data_dict)
df.to_csv("number_squirrels.csv")
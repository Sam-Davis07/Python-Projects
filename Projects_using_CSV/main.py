# with open("weather.csv","r") as file:
#     content = file.readlines()
    
# import csv 

# with open("/Users/Dsam8/OneDrive/Documents/Python Scripts/Udemy/Projects/Projects_using_CSV/weather_data.csv") as data_file:
#     csv_reader = csv.reader(data_file)
#     temperatures = []
#     for row in csv_reader:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)
    
import pandas


data = pandas.read_csv("/Users/Dsam8/OneDrive/Documents/Python Scripts/Udemy/Projects/Projects_using_CSV/weather_data.csv")
print(data)


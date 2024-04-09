
# import csv
#
# with open('./weather_data.csv', 'r') as weather_data:
#     temperatures = []
#     for row in csv.reader(weather_data):
#         temp = row[1]
#         if temp != 'temp':
#             temperatures.append(int(temp))
#     print(temperatures)


import pandas

# Data Frame: A table
weather_frame = pandas.read_csv('weather_data.csv')

# Series: A column
temp_list = weather_frame['temp']

print(temp_list.min())
print(temp_list.max())
print(temp_list.mean())

# Get row in Data
max_temp_row = weather_frame[weather_frame.temp == temp_list.max()]
monday_row = weather_frame[weather_frame.day == 'Monday']

# Convert Cels to Fahr
fahrenheit = monday_row.temp * 9/5 + 32
print(fahrenheit)

# Create data frame
data_dict = {
    'students': ['Amy', 'James', 'Angela'],
    'scored': [76, 56, 65]
}

data_frame = pandas.DataFrame(data_dict)

# Convert to CSV
data_frame.to_csv('new_data.csv')

import pandas

data = pandas.read_csv('squirrels.csv')

fur_counts = data['Primary Fur Color'].value_counts()

gray_count = len(data[data['Primary Fur Color'] == 'Gray'])
red_count = len(data[data['Primary Fur Color'] == 'Cinnamon'])
black_count = len(data[data['Primary Fur Color'] == 'Black'])

color_count_dict = {
    'Fur Color': ['Gray', 'Cinnamon', 'Black'],
    'Count': [gray_count, red_count, black_count]
}

df = pandas.DataFrame(color_count_dict)

df.to_csv('squirrel_count.csv')

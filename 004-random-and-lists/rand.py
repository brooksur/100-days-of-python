import random

# random

rand_int = random.randint(0, 1)
rand_float = random.random()

print(rand_int)
print(rand_float)

# lists

states = ['Utah', 'Idaho', 'Wyoming']

print(states[0])
print(states[1])
print(states[-1])

states.append('Nevada')
print(states)

states.extend(['Arizona', 'New Mexico'])
print(states)

fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
fruits[-1] = "Melons"
fruits.append("Lemons")
print(fruits)

print('hi'[1])
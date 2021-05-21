list1 = list()   # new, empty list

# list(iterable)

# iterable (noun): some object you can iterate over with a for loop

#        literal list (object in memory)
list2 = ["red", 'pink', 'green', 3.2903, None, False, 'blah', 5]

name = "Fred Smith"
list3 = list(name)
list4 = []

print(list1)
print(list2)
print(list3)
print(list4)

names = ['Fred', 'Mark', 'John']
n2 = "Fred, Mark, John"
n3 = n2.split(', ')
print(n2)
print(n3)

print(names[0], n2[0])

cities = ['Berkeley', 'Palo Alto', 'Redwood City', 'Oakland',  'Walnut Creek',
          'Alameda', ]

print(cities[0], cities[4])

cities.append('San Francisco') # one object
cities.append('Mendocino')  # one object
print(cities)
more_cities = ['Sunnyvale', 'Mountain View', 'Santa Jose']
cities.extend(more_cities)  # one iterable
print(cities, '\n')

cities.insert(0, 'Menlo Park')
cities.insert(5, 'Concord')
print(cities, '\n')

my_array = [None] * 100
print(my_array, '\n')

foo = []

print(cities.index('Sunnyvale'))
del cities[10]
print("cities: {}\n".format(cities))
cities.remove('Redwood City')
print("cities: {}\n".format(cities))

city = cities.pop() # remove AND return element -1 (last element)
print(city)
print("cities: {}\n".format(cities))

city = cities.pop(4)  # remove AND return element 4 (5th element)
print(city)
print("cities: {}\n".format(cities))


# LIST.append(), LIST.extend(), LIST.insert()
# del LIST[n]  LIST.remove(VALUE)  LIST.pop(n)
# LIST.index(value)

print(cities.count('Oakland'))

food = ['spam', 'spam', 'spam', 'spam', 'spam', 'spam',
        'spam', 'spam', 'spam', 'spam', 'eggs', 'spam']

print(food.count('spam'), food.count('eggs'))

print(food)
food.remove('spam')
print(food)

print('spam' in food, 'eggs' in food)
print()

print("cities: {}\n".format(cities))

print(cities[0], cities[8], cities[len(cities) - 1], cities[-1])

# print(cities[9])

# START is INclusive  STOP is EXclusive

print(cities[0:5])  # 0, 1, 2, 3, 4
print(cities[:5])   # 0, 1, 2, 3, 4
print(cities[2:6])
print(cities[:5])
print(cities[4:])
print(cities[:])

state = "California"
print(state[:4])
print(state[5:7])
print(state[-3:])
print()

# slice-able: list str tuple bytes
# NOT slice-able: dict set generator

# for VAR ... in ITERABLE:
#    ...

for city in cities:
    # city = next(cities)
    print(city)
print()

word = "abc"
for char in word:
    print(char)
print()

colors = "red:green:blue"
for color in colors.split(':'):
    print(color)
print()

print(cities, '\n')

print(len(cities), min(cities), max(cities))
print(sorted(cities))
print()

for city in reversed(cities):
    print(city)
print()

values = [12, 5, 6, 4, 9, 8, 10, 12, 7, 3, 2, 11, 15]

for city, value in zip(cities, values):
    print(city, value)

print(list(zip(cities, values)), '\n')

print(zip(cities, values))
print(reversed(cities))
print()

zz = zip(cities, values)
print(zz)
cities.append('Santa Rosita')
for city, value in zz:
    print(city, value)
print()

for i, city in enumerate(cities):
    print(i, city)

print(list(enumerate(cities)))

print(['False'] * 10)

print(['foo', 'bar'] + ['spam', 'ham', 'toast'])

tt = 1, 2, 3    # tuple
ll = [4, 5, 6]  # list

print(tt + tuple(ll))
print(list(tt) + ll)

print("Berkeley" in cities)
print("Durham" in cities)

for i in range(10):
    print("*" * i)
print()

for i in range(5, 101, 5):
    print(i, end=' ')
print('\n')

for _ in range(3):
    print("yadda")
print()

print(range(1000000))
print()

for i, city in enumerate(cities, 1):
    print(i, city)
print()
















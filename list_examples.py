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




















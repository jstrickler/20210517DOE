from pprint import pprint
from collections import Counter, defaultdict

d1 = dict()   # empty dict
d2 = {
    'WA': 'Olympia',
    'CA': 'Sacramento',
    'OR': 'Salem',
}
d3 = {}  # empty dict
d4 = dict(WA='Olympia', CA='Sacramento', OR='Salem')

states = ['WA', 'CA', 'OR']
caps = ['Olympia', 'Sacramento', 'Salem']
d5 = dict(zip(states, caps))
print("d2: {}\n".format(d2))
print("d4: {}\n".format(d4))
print("d5: {}\n".format(d5))

airports = {
    'EWR': 'Newark',
    'YYZ': 'Toronto',
    'MCI': 'Kansas City',
    'SFO': 'San Francisco',
    'RDU': 'Raleigh-Durham',
    'SJC': 'San Jose',
    'MCO': 'Orlando',
    'YCC': 'Calgary',
    'ABQ': 'Albuquerque',
    'OAK': 'Oakland',
    'SMF': 'Sacramento',
    'YOW': 'Ottawa',
    'IAD': 'Dulles',
}

print(airports['YOW'])
print(airports.get('PSP'))  # default default is None
print(airports.get('PSP', ''))   # user-defined default is ''

print(airports.setdefault('PSP', 'Palm Springs'))
print("airports: {}\n".format(airports))
print(len(airports))

airports['ONT'] = "Ontario"

print("airports: {}\n".format(airports))
airports['YOW'] = "Ottawa, Canada"

print("airports: {}\n".format(airports))


food = ['spam', 'spam', 'spam', 'spam', 'spam', 'spam',
        'spam', 'spam', 'spam', 'spam', 'spam',
        'eggs', 'spam', 'spam', 'spam', 'spam', 'spam',
        'spam', 'spam', 'spam', 'spam', 'ham',
        'spam', 'spam', 'spam', 'toast']

counts = {}
for f in food:
    # if f not in counts:  # if f is not a key of dict counts
    #     counts[f] = 0   # add f as key with value 0
    counts.setdefault(f, 0)
    counts[f] += 1
#    counts[f] = counts.get(f, 0) + 1  # set counts[f] to counts[f] + 1
print("counts: {}\n".format(counts))

#  see collections.Counter
counts = Counter(food)
print(counts)
print(counts.most_common(3))

# dict  Counter  defaultdict      (obsolete) ordereddict

def zero():
    return 0

my_counter = defaultdict(zero)

my_counter['foo'] = 10
print(my_counter['foo'])
print(my_counter['bar'])


fruits = ["pomegranate", "cherry", "apricot", "apple",
"lemon", "kiwi", "orange", "lime", "watermelon", "guava",
"papaya", "fig", "pear", "banana", "tamarind", "persimmon",
"elderberry", "peach", "blueberry", "lychee", "grape", "date" ]

fruit_lists = defaultdict(list)
for fruit in fruits:
    first_letter = fruit[0]
    fruit_lists[first_letter].append(fruit)

for fruit, fruit_list in fruit_lists.items():
    print(fruit, fruit_list, len(fruit_list))
print()

def p():
    return "Python!"

x = defaultdict(p)

print(x['razzmatazz'])
x['wombat'] = 'Perl!'
print(x['wombat'])
print(x['honey badger'])
print(x)


# for key, value in DICT.items():
#     ...
print(airports.keys())
print(airports.values())
print()

for code, name in sorted(airports.items()):
    print(code, name)

del airports['YCC']
print("airports: ")

pprint(airports)

more_airports = {
    'YOW': 'Ottawa',
    'RIC': 'Richmond',
    'ELM': 'Elmyra/Corning',
}

airports.update(more_airports)

print(airports)



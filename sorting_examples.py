
fruits = ["pomegranate", "cherry", "apricot", "Apple",
"lemon", "Kiwi", "ORANGE", "lime", "Watermelon", "guava",
"Papaya", "FIG", "pear", "banana", "Tamarind", "Persimmon",
"elderberry", "peach", "BLUEberry", "lychee", "GRAPE", "date" ]

f1 = sorted(fruits)
print("f1: {}\n".format(f1))

f2 = sorted(fruits, key=len)
print("f2: {}\n".format(f2))

def to_lower(f):
    return f.lower()


f3 = sorted(fruits, key=to_lower)
print("f3: {}\n".format(f3))

f4 = sorted(fruits, key=str.lower)
print("f4: {}\n".format(f4))


def by_len_and_name(fruit):
    return len(fruit), fruit.lower()

f5 = sorted(fruits, key=by_len_and_name)
print("f5: {}\n".format(f5))

nums = [800, 80, 1000, 32, 255, 400, 5, 5000]

n1 = sorted(nums)
print("n1: {}\n".format(n1))

people = [
    ('Melinda', 'Gates', 'Gates Foundation', '1964-08-15'),
    ('Steve', 'Jobs', 'Apple', '1955-02-24'),
    ('Larry', 'Wall', 'Perl', '1954-09-27'),
    ('Paul', 'Allen', 'Microsoft', '1953-01-21'),
    ('Larry', 'Ellison', 'Oracle', '1944-08-17'),
    ('Bill', 'Gates', 'Microsoft', '1955-10-28'),
    ('Mark', 'Zuckerberg', 'Facebook', '1984-05-14'),
    ('Sergey','Brin', 'Google', '1973-08-21'),
    ('Larry', 'Page', 'Google', '1973-03-26'),
    ('Linus', 'Torvalds', 'Linux', '1969-12-28'),
]

for person in sorted(people):
    print(person)
print('-' * 60)

def by_dob(p):
    return p[3], p[1], p[0]

for person in sorted(people, key=by_dob):
    print(person)
print('-' * 60)

for person in sorted(people, key=lambda p: p[3]):
    print(person)
print('-' * 60)


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

for code, name in sorted(airports.items()):
    print(code, name)
print('-' * 60)

for code, name in sorted(airports.items(), key=lambda e: (e[1], e[0])):
    print(code, name)
print('-' * 60)

def by_value(item):
    return item[1], item[0]

for code, name in sorted(airports.items(), key=by_value):
    print(code, name)
print('-' * 60)


for code, name in sorted(airports.items(), key=by_value, reverse=True):
    print(code, name)
print('-' * 60)

fruits = ["pomegranate", "cherry", "apricot", "apple",
"lemon", "kiwi", "orange", "lime", "watermelon", "guava",
"papaya", "fig", "pear", "banana", "tamarind", "persimmon",
"elderberry", "peach", "blueberry", "lychee", "grape", "date" ]


fruits.sort()
print(fruits)








fruits = ["pomegranate", "cherry", "apricot", "apple",
"lemon", "kiwi", "orange", "lime", "watermelon", "guava",
"papaya", "fig", "pear", "banana", "tamarind", "persimmon",
"elderberry", "peach", "blueberry", "lychee", "grape", "date" ]

f0 = []
for f in fruits:
    f0.append(f.upper())
print("f0: {}\n".format(f0))

#  [EXPR for VAR ... in ITERABLE if CONDITION]
f1 = [f.upper() for f in fruits]
print("f1: {}\n".format(f1))

# result = [ variation-of-element for element in original-iterable if some-condition-of-element]
f2 = [f.upper() for f in fruits if f.startswith('p')]
print("f2: {}\n".format(f2))

f3 = [f for f in fruits if f.startswith('p')]
print("f3: {}\n".format(f3))

nums = [800, 80, 1000, 32, 255, 400, 5, 5000]
n1 = [n for n in nums if n > 300]
print("n1: {}\n".format(n1))

n2 = [float(n) * 2 for n in nums]
print("n2: {}\n".format(n2))

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

last_names = [p[1] for p in people]
print("last_names: {}\n".format(last_names))

data = [f"{p[0]} {p[1]}: {p[3].split('-')[0]}" for p in people]
print("data: {}\n".format(data))

food = ['spam', 'spam', 'spam', 'spam', 'spam', 'spam',
        'spam', 'spam', 'spam', 'spam', 'spam',
        'eggs', 'spam', 'spam', 'spam', 'spam', 'spam',
        'spam', 'spam', 'spam', 'spam', 'ham',
        'spam', 'spam', 'spam', 'toast']

good_food = [f for f in food if f != 'spam']
print("good_food: {}\n".format(good_food))


a = ['a', 'b', 'c']
b = [5, 10, 15]

s = [[a, b] for a, b in zip(a, b)]
print(s)

s = [list(x) for x in zip(a, b)]
print(s)

powers = [(i, i**2, i**3) for i in range(10)]
print(powers)

young_billionaires = [(p[0], p[1]) for p in people if p[3] > '1970']
for person in young_billionaires:
    print(person)
print()

fgen = (f.upper() for f in fruits)
print(fgen)


for fruit in fgen:
    print(fruit)
print()

fruits.append('lychee')
fruits.append('marionberry')

print("round 2")
for fruit in fgen:
    print(fruit)

print()
fgen = (f.upper() for f in fruits)
short_fruits = [f[:3] for f in fgen]
print("short_fruits: {}\n".format(short_fruits))

print(list(fgen))





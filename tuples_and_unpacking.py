from collections import namedtuple

# collection of related items
person = 'Bill', 'Gates', 'Microsoft', '1955-10-28'
print(person)
print(type(person))
print(person[0])
print(person[:2])
print()

# tuples for records or structs
# lists for looping

# old: named tuples  (add field names)
# new: data classes (field names, mutable, flexible)

Person = namedtuple('Person', "first_name last_name product dob")
Person = namedtuple('Person', ["first_name", "last_name", "product", "dob"])

p = Person('Bill', 'Gates', 'Microsoft', '1955-10-28')
print(p[0], p.first_name, p.dob)

p2 = p._replace(product="Apple")
print(p2)

p = Person('Tim', 'Cook', 'Apple', None)
print(p.first_name, p.last_name)
print(type(p).__name__)

d = p._asdict()
print(d['first_name'], '\n')

#  var, var, ... = iterable
first_name, last_name, product, dob = person  # unpacking
print(first_name, last_name)

s = ["Palo Alto", "California", "USA"]
city, state, country = s
print(city, country)

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

print(people[0])
print(people[0][0])
print(people[0][0][0])
print()

for person in people:
    print(person[0], person[1])
print('-' * 60)

for person in people:
    first_name, last_name, product, dob = person
    print(first_name, last_name)
print('-' * 60)

# **** IMPORTANT ****
for first_name, last_name, product, dob in people:
    # first_name, last_name, product, dob = next(people)
    print(first_name, last_name)
print('-' * 60)

data = [(5, 4.9), (8, 3.6), (1, 9.8)]
for a, b in data:
    print(a, b)
print('-' * 60)

values = ['a', 'b', 'c', 'd', 'e', 'f']
x, y, *z = values
print(x, y, z)

x, *y, z = values
print(x, y, z)

*x, y, z = values
print(x, y, z)


people = [
    ('Melinda', 'Gates', 'Gates Foundation', 'Microsoft', '1964-08-15'),
    ('Steve', 'Jobs', 'Apple', 'NeXT', '1955-02-24'),
    ('Larry', 'Wall', 'Perl', '1954-09-27'),
    ('Paul', 'Allen', 'Microsoft', '1953-01-21'),
    ('Larry', 'Ellison', 'Oracle', '1944-08-17'),
    ('Bill', 'Gates', 'Microsoft', '1955-10-28'),
    ('Mark', 'Zuckerberg', 'Facebook', '1984-05-14'),
    ('Sergey','Brin', 'Google', '1973-08-21'),
    ('Larry', 'Page', 'Google', '1973-03-26'),
    ('Linus', 'Torvalds', 'Linux', 'Git', '1969-12-28'),
]

for first_name, last_name, *product, dob in people:
    print(last_name, product)
print()

nt_list = []
for first_name, last_name, *product, dob in people:
    nt_list.append(Person(first_name, last_name, product, dob))

print(nt_list, '\n')

for first_name, last_name, product, dob in nt_list:
    print(last_name, product)
print()

t3 = 1, 2, 3
t2 = 1, 2
t1 = 1,
t0 = ()









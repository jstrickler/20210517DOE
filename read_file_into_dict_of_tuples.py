from pprint import pprint
info = {}

with open('DATA/knights.txt') as knights_in:
    for raw_line in knights_in:
        line = raw_line.rstrip()
        name, title, color, quest, comment = line.split(':')
        info[name] = [title, color, quest, comment]

pprint(info)

print(info['Arthur'][2])
print(info['Galahad'][0])
print()

for name, data in info.items():
    print(name, data)
print()

for name, data in info.items():
    print(data[0], name)
print()

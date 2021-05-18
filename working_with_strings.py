
actor = "Chris Hemsworth"

print(actor.upper())
print(actor.lower())
print(actor.count('h'))
print(actor.startswith('Chr'))
print(actor.startswith("Liam"))
print(actor.endswith('worth'))
print(actor.replace('Chris', 'Liam'))
print(actor)
chu = actor.upper()
print(chu)
print(len(actor))
# print(__builtins__.len(actor))

a = 'foo'
b = 'bar'
c = a + b
print(c)

print(actor.find('Chris'))
print(actor.find('Liam'))
print(actor.find('worth'))
print(actor.find('value'))

print(actor.count('h'))
print(actor.lower().count('h'))

names = actor.split()
print(names)

log_record = '2021:05:17'
print(log_record.split(':'))

name = "William   Henry    Harrison"
print(name.split())   #  \s+
print(name.split(' '))

food = 'Pad Thai    '
trimmed = food.rstrip()
print(trimmed + "<")

s = "     All my exes live in Texas    "
print('|' + s.lstrip() + '|')
print('|' + s.rstrip() + '|')
print('|' + s.strip() + '|')
print()

s = "xyxyxxxyyyxxyyAll my exes live in Texasyyyyyyyyyyyyyx"
print('|' + s.lstrip('xy') + '|')
print('|' + s.rstrip('xy') + '|')
print('|' + s.strip('xy') + '|')
print()

m = "spam\n"

print(m)
print('ok')
print(m.rstrip())
print('ok')













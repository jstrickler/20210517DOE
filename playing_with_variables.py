
color = "blue"
animal = 'wombat'
country = 'Burkina Faso'

def spam():
    print("spam! SPAM! SSPPAAMM!!!!!!!!")

print(color)
print(animal)
print(country)
print()

# user_input = input("Enter variable to print: ")
# print(user_input)

g = globals()
# print(g[user_input])

print(g['spam'])

g['spam']()

name = 'Bob'
print(g['name'])


g['bark'] = lambda : print("woof")

bark()

g['ocean'] = 'Atlantic'
print(ocean)

print(g)
print('-' * 60)
print(dir(__builtins__))

print(__builtins__.len(g))
print(__builtins__.len(dir(__builtins__)))

x = [1, 2, 3]
print(dir(x))

print(dir(object))
print(dir(None))
print(dir(dir))


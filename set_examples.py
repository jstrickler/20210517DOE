
colors1 = ['red', 'green', 'white', 'purple', 'red', 'blue', 'blue', 'pink']
colors2 = ['purple', 'pink', 'ecru', 'red', 'red', 'black', 'blue']

c1 = set(colors1)
c2 = set(colors2)

c1.add('orange')
c1.add('orange')

print("c1: {}\n".format(c1))
print("c2: {}\n".format(c2))

print("common:", c1 & c2)  # intersection
print("not common:", c1 ^ c2)  # Xor (not common)
print("ALL (unique)", c1 | c2)  # union
print("only c1:", c1 - c2)
print("only c2:", c2 - c1)
print("len(c1)", len(c1))
for color in 'orange', 'black', 'brown', 'tan', 'grey', 'blue':
    print(color, color in c1)






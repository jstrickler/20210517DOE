fruits = ["pomegranate", "cherry", "apricot", "apple",
"lemon", "kiwi", "orange", "lime", "watermelon", "guava",
"papaya", "fig", "pear", "banana", "tamarind", "persimmon",
"elderberry", "peach", "blueberry", "lychee", "grape", "date" ]

f_upper = [f.upper() for f in fruits]
print("f_upper: {}\n".format(f_upper))

f_gen = (f.upper() for f in fruits)
print(f_gen)

f = next(f_gen)
print(f)
f = next(f_gen)
print(f)
print('---')
for fruit in f_gen:
    print(fruit)
    if fruit == 'ELDERBERRY':
        break
print('---')
f = next(f_gen)
print(f)

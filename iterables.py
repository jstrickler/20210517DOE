
x = [1, 2, 3, 4, 5]   # iterABLE

# "just works"
for value in x:
    print(value)
print()

# the hard way -- don't do this
i = iter(x)   # iterATOR
for v in i:
    print(v)
print()

i = iter(x)
print(next(i))
print(next(i))
print()

with open('DATA/mary.txt') as mary_in:
    for raw_line in mary_in:
        print(raw_line.rstrip())
print()


with open('DATA/mary.txt') as mary_in:
    first_line = next(mary_in)
    print(first_line.rstrip())
    print("---")
    for line in mary_in:
        print(line.rstrip())
print()


with open('DATA/mary.txt') as mary_in:
    print(next(mary_in).rstrip())
    print(next(mary_in).rstrip())
    print(next(mary_in).rstrip())
    print(next(mary_in).rstrip())

#    print(next(mary_in).rstrip())


print()



with open('DATA/mary.txt') as mary_in:
    # faux for loop
    while True:
        iterator = iter(mary_in)
        try:
            line = next(iterator)
            print(line.rstrip())
        except StopIteration:
            break
print()



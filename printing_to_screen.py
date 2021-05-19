import sys
print("Hello, world")

print("Hello,", "world")

a = 5
b = 10
c = 15
d = 20
print(a, b)
# print(str(a), str(b))

# print(str(a) + SEP + str(b) + END)

print(a, end=' ')
print(b)
print(a, end='')
print(b, end='')
print("OK")
print(a, b, sep="/")
print(a, b, sep='')
print(a, b, c, d, sep="<=>")
print()
print('\n')
print("Wow.")
# print(end='')  superfluous

# print(...., end='\n', sep=' ', flush=False, file=sys.stdout)
print("Uh-oh", file=sys.stderr)






x = 123
xx = str(123)
print(x, xx)
print(type(x), type(xx))
print(repr(x), repr(xx))

y = "123"
print(y * 5)
z = int(y)
print(z * 5)
print(type(y), type(z))

r = "1234"
print(int(r) * 5)

m = "DeadBeef"
print(int(m, 16))

print(bool(r), bool(m), bool(0))

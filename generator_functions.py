
def gfun():
    print("starting")
    yield 'a'
    yield 'b'
    yield 'c'

g = gfun()
print(next(g))
print("--")
print(next(g))
print("--")
print(next(g))
print('-' * 60)
g = gfun()
for i in g:
    print(i)


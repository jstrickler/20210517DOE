# C, C++, Java, C#, awk, Perl, scala, kotlin, PHP

value = 56

# if else elif while for try except finally
# with def class async...

if value > 75:
    print("wombat")  # Indent 4 spaces. It feels good.
    print("quokka")
elif value > 50:
    print("platypus")
    print("wallaby")
elif value > 25:
    print("blue-ringed octopus")
    print("crocodile")
else:
    print("kangaroo")
    print("kookaburra")

print("Done.")

# X is False if
#    X is False
#    X is None
#    X = 0 or X = 0.0
#    len(X) = 0

country = "Canada"

# ternary
color = "red" if country == 'Canada' else "green"
#  color = (country == 'Canada')?'red':'green'
print(color)

if country == 'Canada': color = 'red'  # OK

#  == is != > < >= <=

# if blah is None:
#     ....

# not and or

m = 5.993

if isinstance(m, float):
    print("it's a float")

class A:
    pass

class B(A):
    pass

class C(B):
    pass

c1 = C()
print(isinstance(c1, C))
print(isinstance(c1, B))
print(isinstance(c1, A))
print(issubclass(B, A))

print(type(A))
b1 = B()
a1 = A()
print(type(b1), type(a1))
print(type(b1) == type(a1))







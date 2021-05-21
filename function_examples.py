

def get_message():
    return "Hello DOE world"

m = get_message()
print(m)

def print_message():
    message = get_message()
    print(message)
    # return None


print_message()


def double(x):
    return 2 * x


print(double(2))
print(double('mint'))
print(double(['trouble']))
print(double(x=100))


#        req     opt   req      opt
#        positional    named
def wacky(p1, p2, *p3, p4, p5, **p6):
    print(p1)
    print(p2)
    print(p3)
    print(p4)
    print(p5)
    print(p6)
    print()

wacky('a', 'b', 'c', 'd', 'e', p4='f', p5='g')

def less_wacky(p1, p2, *p3):
    print(p1, p2, p3)

less_wacky('a', 'b', 'c', 'd', 'e')
less_wacky('a', 'b')

def wackier(*, p1, p2):  # Keyword-only args
    print(p1, p2)

wackier(p1='a', p2='b')
wackier(p2='a', p1='b')

def spam(user, file_name):
    print("user:", user)
    print("file_name:", file_name)

spam(file_name="wombat.txt", user="Crocodile Dundee")

def config(**kwargs):
    print(kwargs)
    if 'color' in kwargs:
        print(kwargs.get('color'))

config(file_name="wombats.txt", user_name="Mantovani", color="orange",
       dinosaur="triceratops")


def doit(*things):
    print("things:", things)

doit()
doit(1, 2)
doit('a', 'b', 'c')


def generic(*args, **kwargs):
    print("args:", args)
    print("kwargs:", kwargs)
    print()


pos_data = [1, 2, 3, 4]

named_data = {
    'color': 'blue',
    'continent': 'Asia',
    'country': 'Nepal',
}

generic(*pos_data, **named_data)

def hello(whom="world"):
    print("Hello,", whom)

hello()
hello('Mom')
hello('Dolly')














import logging
from functools import wraps, lru_cache

logging.basicConfig(
    format='%(name)s %(asctime)s %(levelname)s %(message)s',  # <1>
    filename='decorators.log',
    level=logging.DEBUG,

)

def log_calls(orig_func):

    @wraps(orig_func)
    def _(*args, **kwargs):
        logging.debug(f"Called {orig_func.__name__}")
        return orig_func(*args, **kwargs)

    return _

@log_calls
def spam():
    print("Spam!")
# spam = log_calls(spam)

@log_calls
def ham():
    print("Ham!")
# ham = log_calls(ham)


spam()
ham()

def goofy(func):
    return 42

@goofy
def toast():
    print("Wokka-wokka")

print(toast)



# @apple
# def peach():
#    pass
# EXACTLY THE SAME AS
# peach = apple(peach)

print(spam.__name__, ham.__name__)


@lru_cache(1000)
def add(x, y):
    print(f"Calling add({x}, {y})")
    return x + y  # could be involved calculation here ...

data = [(5, 3), (4, 10), (5, 3), (5, 3), (13, 9)]

for i, j in data:
    print(add(i, j))



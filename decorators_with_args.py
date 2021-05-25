

#  @foo
#  def bar():
#     pass

#  bar = foo(bar)

# =============================
#  @foo(a, b, c)
#  def bar():
#     pass

# bar = foo(a, b, c)(bar)
from functools import wraps

def animal_noise(noise):

    def deco(old_func):

        @wraps(old_func)
        def _(*args, **kwargs):
            print(noise * 10)
            return old_func(*args, **kwargs)

        return _

    return deco

@animal_noise("woof woof")
def spam():
    print("spam!")
# spam = animal_noise("woof woof")(spam)

@animal_noise("meow")
def ham():
    print("ham!")

@animal_noise("roarrrrr")
def toast():
    print("toast!")

spam()
spam()
toast()
ham()
toast()

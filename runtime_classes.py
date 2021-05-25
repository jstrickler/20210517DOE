
class Animal:
    pass

class Cat(Animal):
    FOOD = 'Any animal'
    def meow(self):
        print("meow! meow!")

c = Cat()
c.meow()

def bark(self):
    print("woof! woof!")

Dog = type('Dog', (Animal,), {'bark': bark, 'fetch': lambda self: print("fetching..."), 'FOOD': 'anything, preferably stinky'})

d = Dog()
d.bark()
d.fetch()
print(d.FOOD)


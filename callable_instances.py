

def spam():
    print("Whoo-hoooooo")


spam()  # functions are callables


class Ham:
    pass


h = Ham()   # classes are callables

x = 5

class zombify:
    def __init__(self, title):
        self._title = title

    def __call__(self):
        return f"{self._title} and Zombies"

ja = zombify("Pride and Prejudice")

print(ja())









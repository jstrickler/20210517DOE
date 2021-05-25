#!/usr/bin/env python
import types

class Knight():
    def __init__(self, name, title, color):
        self._name = name
        self._title = title
        self._color = color

    @property  # <1>
    def name(self):  # <2>
        return self._name

    @property
    def color(self):
        return self._color

    @color.setter  # <3>
    def color(self, color):
        self._color = color

    @property
    def title(self):
        return self._title


if __name__ == '__main__':
    k = Knight("Lancelot", "Sir", 'blue')

    print(k)
    print(k.name, k.title, k.color)

    attr_names = ['name', 'title', 'color']

    print(getattr(k, 'name'))
    print()

    for aname in attr_names:
        print(aname, getattr(k, aname))
    print()

    if hasattr(k, 'title'):
        print(getattr(k, 'title'))

    # ....
    def custom_jsonify(x):
        pass

    if hasattr(k, 'to_json'):
        json_string = k.to_json()
    else:
        json_string = custom_jsonify(k)

    # getattr()  hasattr()  setattr() delattr()

    setattr(Knight, 'joust', lambda self: print("JOUSTING!"))

    k.joust()

    def fight(self):
        print("Fighting fighting fighting, then off for a spot of tea.")

    setattr(k, 'fight', types.MethodType(fight, Knight))

    k.fight()

    k2 = Knight('Arthur', 'king', 'green')
    k2.joust()

    k2.fight()

#!/usr/bin/env python
import inspect
import typing as T

class Spam:  # <1>
    pass

Numeric = T.Union[int, float]

def toast(items: T.Iterable, factor: Numeric) -> T.List[int]:
    x = [1, 2, 3]
    return 42






def ham(p1: int, p2: str='a', *p3:int, p4: float, p5: str='b', **p6) -> None:  # <2>
    print(p1, p2, p3, p4, p5, p6)

ham(5, 'b', 6, 6, 6, p4=5.9, p5="woohoo", animal='peahen', country="Tuvalu")

ham('a', 'b', 'b', 'c', 'd', p4='e', p5=4, animal=5.9, country="Tuvalu")



for thing in (inspect, Spam, ham):
    print("{}: Module? {}. Function? {}. Class? {}".format(
        thing.__name__,
        inspect.ismodule(thing),  # <3>
        inspect.isfunction(thing),  # <4>
        inspect.isclass(thing),  # <5>
    ))

print()

print("Function spec for Ham:", inspect.getfullargspec(ham))  # <6>
print()

print("Current frame:", inspect.getframeinfo(inspect.currentframe()))  # <7>

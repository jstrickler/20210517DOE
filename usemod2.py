# from pkg.pkg.module import NAME
from doeclass.utils.doelib import spam, ham, ANIMALS, Jam, this_is_a_bad_name
from doeclass.utils import doelib

ANIMALS.append("kangaroo")

ANIMALS = ['pine marten',
           'honey badger']

ham()
spam()
j = Jam()
t = this_is_a_bad_name()
print(j, t)

print(ANIMALS)
print(doelib.ANIMALS)



import sys
# from pkg.pkg import module
from doeclass.utils import doelib


# find doelib.py and execute it
# find doeclass/utils/doelib.py and execute it

def _toast():
    print("local toast!")

doelib.spam()
doelib.ham()
# doelib._toast() naughty programmer
_toast()

for path in sys.path:
    print(path)


print(doelib.ANIMALS[0])

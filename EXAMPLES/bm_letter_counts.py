#!/usr/bin/env python
import timeit

setup_code = """
import re
alice_text = open('../DATA/alice.txt').read()
"""

codes = [
    '''count = alice_text.count('a') + alice_text.count('A')''',
    '''count = alice_text.lower().count('a')''',
    '''count = len(re.findall(r'[aA]', alice_text))''',
    '''count = len(re.findall('a', alice_text, re.I))''',
    '''
count = t = alice_text.encode()
count = t.count(65) + t.count(97)
    ''',
]

for code in codes:
    t = timeit.Timer(code, setup_code)
    print(code, '\n')
    print(t.timeit(1000))
    print()

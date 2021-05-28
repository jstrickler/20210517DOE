#!/usr/bin/env python

import timeit

setup_code = """
import read_file_into_dict_of_tuples
"""

codes = [
    '''main()''',
]

for code in codes:
    t = timeit.Timer(code, setup_code)
    print(code, '\n')
    print(t.timeit(1))
    print()

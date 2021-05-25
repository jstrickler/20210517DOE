#!/usr/bin/env python

def trimmed(file_name):
    with open(file_name) as file_in:
        for line in file_in:
            yield line.rstrip('\n\r')  # <1>


t = trimmed('../DATA/mary.txt')
print(t, '\n')

for trimmed_line in t:  # <2>
    print(trimmed_line)
print()

t = trimmed('../DATA/mary.txt')
print(next(t))
print(next(t))

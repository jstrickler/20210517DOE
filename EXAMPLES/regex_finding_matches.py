#!/usr/bin/env python

import re

s = """lorem ipsum M-302 dolor sit amet, consectetur r-99 adipiscing elit, sed do
 eiusmod tempor incididunt H-476 ut labore et dolore magna Q-51 aliqua. Ut enim 
ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex  
ea commodo z-883  consequat. Duis aute irure dolor in reprehenderit in
voluptate velit esse cillum dolore U901 eu fugiat nulla pariatur. 
Excepteur sint occaecat A-110 cupidatat non proident, sunt in H-332 culpa qui 
officia deserunt Y-45 mollit anim id est laborum"""

pattern = r'[A-Z]-\d{2,3}'  # <1>

# date_strings = "Apr 5, 2022", "2022-04-05", "4/5/2022"
# date_pattern = r'(?:(?P<month>[A-Z][a-z]{2}) (?P<day>\d{1,2}), (?P<year>\d{4})|(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2})|(?P<month>\d{1,2})/(?P<day>\d{1,2})/(?P<year>\d{2}))'
#
# for date_string in date_strings:
#     m = re.search(date_pattern, date_string)
#     if m:
#         print("FOUND:", m.group("month"), m.group("day"), m.group("year"))


if re.search(pattern, s):  # <2>
    print("Found pattern.")
print()

m = re.search(pattern, s)  # <3>
print(m)
if m:
    print("Found:", m.group(0))  #  m.group() also works
print()

for m in re.finditer(pattern, s):  # <5>
    print(m.group())
print()

matches = re.findall(pattern, s)  # <6>
print("matches:", matches)


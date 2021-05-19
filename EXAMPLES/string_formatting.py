#!/usr/bin/env python

name = "Tim"
count = 5
avg = 3.4562309302
info = 2093

# printf()-like
print("Name is %s and count is %d" % (name, count))  # "legacy" AKA Python 2.x


print("Name is {} and count is {}".format(name, count))
print("{} {}".format(name, count))

print("Name is [{:<10s}]".format(name))  # <1>
print("Name is [{:>10s}]".format(name))  # <2>
print("Name is [{:^10s}]".format(name))  # <2>
print("count is {:03d} avg is {:.2f}".format(count, avg))  # <3>
print("count is {:3d} avg is {:.2f}".format(count, avg))  # <3>

print("info is {0} {0:d} {0:o} {0:x} {0:b}".format(info))  # <4>
print("info is {0} {0:d} {0:#o} {0:#x} {0:016b}".format(info))  # <5>

print("${:,d}".format(38293892))  # <6>

print("It is {temp} in {city}".format(city='Orlando', temp=85))  # <7>
print()

# f-strings
print(f"Name is {name} and count is {count}")
print(f"count is {count:03d} avg is {avg:.2f}")  # <3>
value = 38293892
print(f"${value:,d}")  # <6>

temperature = 7

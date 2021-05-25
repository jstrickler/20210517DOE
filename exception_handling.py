import signal

file_name = "wombats.txt"

try:
    with open(file_name) as wombats_in:
        for line in wombats_in:
            print(line.rstrip())
except OSError as err:
    print('Sorry, unable to open your file -- using default data')
    print(err)


print("continuing...")

values = ['a', 'b', 'c']
try:
    print(values[5])
except IndexError as err:
    print(err)
print("continuing...")

nums = [0, 5.3, 17.6, "2.32", 0.0, "ABC", 18.4, 6.9]
for n in nums:
    try:
        result = 26 / float(n)
    except Exception as err:
        print(err, type(err).__name__)
    else:
        print(result)

import sqlite3

conn = None
try:
    conn = sqlite3.connect('DATA/presidents.db')
except (sqlite3.OperationalError, sqlite3.DatabaseError) as err:
    print(err)
    exit()
else:
    cursor = conn.cursor()
    cursor.execute("select firstname, lastname from presidents")
    for row in cursor.fetchall():
        print(row)
finally:
    if conn:
        conn.close()





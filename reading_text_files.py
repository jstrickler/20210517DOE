
mary_in = open('DATA/mary.txt')
# ... read file
mary_in.close()

with open('DATA/mary.txt') as mary_in:
    for raw_line in mary_in: # mary_in.readline()
        line = raw_line.rstrip()
        print(line)
print('-' * 60)

with open('DATA/mary.txt') as mary_in:
    entire_file = mary_in.read()  # read the whole file
    print("NORMAL:")
    print(entire_file)
    print("RAW:")
    print(repr(entire_file))
print('-' * 60)

with open('DATA/mary.txt') as mary_in:
    lines_with_nl = mary_in.readlines()
    print(lines_with_nl)
print('-' * 60)

with open('DATA/mary.txt') as mary_in:
    lines_without_nl = [line.rstrip() for line in mary_in]
    print(lines_without_nl)

with open('DATA/alice.txt') as alice_in:
    for raw_line in alice_in:
        if 'rabbit' in raw_line.lower():
            print(raw_line.rstrip())
print('-' * 60)

count = 0
with open('DATA/words.txt') as words_in:
    for raw_line in words_in:
        line = raw_line.rstrip()
        if line.endswith('q'):
            count += 1
print("Count is", count)




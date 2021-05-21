fruits = ["pomegranate", "cherry", "apricot", "apple",
"lemon", "kiwi", "orange", "lime", "watermelon", "guava",
"papaya", "fig", "pear", "banana", "tamarind", "persimmon",
"elderberry", "peach", "blueberry", "lychee", "grape", "date" ]

with open('fruitlist.txt', 'w') as fruitlist_out:
    for fruit in fruits:
        fruitlist_out.write(fruit + '\n')


with open('DATA/words.txt') as words_in:
    with open('qwords.txt', 'w') as qwords_out:
        for line in words_in:
            if 'q' in line:
                qwords_out.write(line)
                qwords_out.flush()
                # print(line, file=qwords_out, flush=True, end='')

file_paths = ['DATA/alice.txt',  'DATA/words.txt']
# pattern = sys.argv[1]
# file_paths = sys.argv[2:]
file_objects = []
for file_path in file_paths:
    file_objects.append(open(file_path))
# work with files here....
for file_object in file_objects:
    file_object.close()

# CSV JSON  ???




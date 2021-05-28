"""
Read data from knights.txt
"""
from pprint import pprint

def main():
    kdata = read_data()
    pretty_print(kdata)
    print(get_item(kdata, 'Arthur', 2))
    print_items(kdata)
    print_title_name(kdata)


def read_data():
    """
    Read data from colon-delimited file.

    Blah blah blah-dy blah


    :return: knight data as dict where keys are field names
    """
    info = {}

    with open('DATA/knights.txt') as knights_in:
        for raw_line in knights_in:
            line = raw_line.rstrip()
            name, title, color, quest, comment = line.split(':')
            info[name] = [title, color, quest, comment]
    return info

def pretty_print(data):
    pprint(data)
    print()

def get_item(data, knight, field_number):
    return data[knight][field_number]

def print_items(data):
    for name, data in data.items():
        print(name, data)
    print()

def print_title_name(data):
    for name, knight_data in data.items():
        print(knight_data[0], name)
    print()

if __name__ == '__main__':
    main()

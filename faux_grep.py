import sys
import fileinput
import argparse
import re

# python faux_grep.py -i -f bird DATA/alice.txt DATA/parrot.txt

description = """
faux grep

This is a humble emulation of the mighty *ix *grep* command. 

Use it and enjoy.

"""
parser = argparse.ArgumentParser(description=description)

parser.add_argument("-i", dest="ignore_case", action="store_true", help="Ignore case")
parser.add_argument("-f", dest="show_filename", action="store_true", help="Show file name")
parser.add_argument("pattern", help="Pattern to find")
parser.add_argument("files", nargs="*", help="Files to search")

args = parser.parse_args()

pattern = re.compile(args.pattern, re.I if args.ignore_case else 0)

print(args)

for raw_line in fileinput.input(args.files):
    if pattern.search(raw_line):
        if args.show_filename:
            print(fileinput.filename(), end=' ')
        line = raw_line.rstrip()
        print(line)






"""
while (my $line = <>) {
}
"""

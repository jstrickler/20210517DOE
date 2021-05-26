from glob import glob

#  *.txt  s[a-z]_report.txt   spam.*    *.*     *_*

print("glob('DATA/*.txt'): {}\n".format(glob('DATA/*.txt')))

print("glob('DATA/wombats.*'): {}\n".format(glob('DATA/wombats.*')))

print("glob('*.py'): {}\n".format(glob('*.py')))




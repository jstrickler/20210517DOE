import sys

print(sys.argv)  # command name + all arguments  (list)

print(sys.argv[0]) # command name

# pattern = sys.argv[1]
# files = sys.argv[2:]
# for file_name in files:
#    ...

if len(sys.argv) >= 3:
    print(sys.argv[1])  # first arg
    print(sys.argv[2])  # second arg
else:
    print("please specify 2 args")



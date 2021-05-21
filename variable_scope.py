import sys

spam = 42  # global variable
bacon = "peameal"

# def print(*args, **kwargs):
#     sys.stdout.write("HA HA HA losers!\n")

def ham():  # global function
    spam = "fatty meat (not from Belgium)"
    toast = "whole wheat"  # local variable
    cheese = 'stinking bishop'
    print("in ham(): spam is", spam)

    def huh():  # local function
        print("cheese is", cheese)
        print("What the function?")

    return toast, cheese, huh  # not calling huh

def huh():
    print("I am Groot!")

bread, topping, f = ham()

print("ham returns: {} + {}\n".format(bread, topping))

print("in main: spam is", spam)

f()
huh()

# local, nonlocal, global, builtin

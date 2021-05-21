"""
Misc DOE utilities

spam -- blah blah
ham -- blah blah
"""
ANIMALS = ['wombat', 'koala', 'platypus',
        'quokka']

# I should not change spam() and ham()
# without notification
def spam(num=0):
    """
    Fatty, fatty, meat! Good on crackers or for sushi.

    :param num: number of pieces of sushi
    :return: None
    """
    print("Hello from spam()")

def ham():
    """
    Super-delicious smoked leg of swine. Highly recommended.

    :return: None
    """
    print("Hello from ham()")
    print("Animal:", ANIMALS[-1])
    _toast()

# I don't have to tell you about
# changes to _toast()
def _toast():  # pseudo-private
    print("   ...and _toast()")

# good juju
class Jam:
    """
    A Jam class for toast. Or musical improvisation.
    Or other stuff.

    Yadda yadda yadda
    """
    pass

# bad juju
class this_is_a_bad_name:
    pass

print("My name is", __name__)

# if running directly, NOT imported
if __name__ == '__main__':
    print("Hi mom!!")

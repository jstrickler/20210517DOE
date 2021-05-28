"""
Play a game of cards
"""

from carddeck import CardDeck
from jokerdeck import JokerDeck

DEALER_1 = CardDeck("Wanda")
print(DEALER_1)

# print(DEALER_1._dealer) # naughty!

# <suspicious>
DEALER_1.color = "blue"
DEALER_1.animal = "wombat"

print(DEALER_1)
print(DEALER_1.color)

CardDeck.place = "Durham"

print(CardDeck.place)
print(DEALER_1.place)
# </suspicious>
print(CardDeck.mro())

# print("method:", d1.get_dealer())

print("property:", DEALER_1.dealer)
print(type(DEALER_1.dealer))

DEALER_1.dealer = "Vision"
print(DEALER_1.dealer)

try:
    DEALER_1.dealer = 123.456  # call property setter
    print(DEALER_1.dealer)
except TypeError as err:
    print(err)

print(DEALER_1.dealer_upper) # call property getter

try:
    DEALER_2 = CardDeck(1234)
    print(DEALER_2.dealer)
except TypeError as err:
    print(err)

print()
DEALER_1.shuffle()
print(DEALER_1.cards, '\n')

for _ in range(5):
    print(DEALER_1.draw())
print()

print(CardDeck.RANKS)
print(DEALER_1.RANKS)

print(DEALER_1.get_ranks())
print(CardDeck.get_ranks())
print()

JOKER_1 = JokerDeck("Jerry")
print(JOKER_1)
JOKER_1.shuffle()
print(JOKER_1.cards)

print(len(DEALER_1), len(JOKER_1))
print(CardDeck.__len__(DEALER_1))

print(DEALER_1, JOKER_1)
print(str(DEALER_1), str(JOKER_1))

NEW_DECK = DEALER_1 + JOKER_1
print(NEW_DECK)

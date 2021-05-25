from carddeck import CardDeck
from jokerdeck import JokerDeck

d1 = CardDeck("Wanda")
print(d1)

print(d1._dealer) # naughty!

# <suspicious>
d1.color = "blue"
d1.animal = "wombat"

print(d1)
print(d1.color)

CardDeck.place = "Durham"

print(CardDeck.place)
print(d1.place)
# </suspicious>
print(CardDeck.mro())

# print("method:", d1.get_dealer())

print("property:", d1.dealer)
print(type(d1.dealer))

d1.dealer = "Vision"
print(d1.dealer)

try:
    d1.dealer = 123.456  # call property setter
    print(d1.dealer)
except TypeError as err:
    print(err)

print(d1.dealer_upper) # call property getter

try:
    d2 = CardDeck(1234)
    print(d2.dealer)
except TypeError as err:
    print(err)

print()
d1.shuffle()
print(d1.cards, '\n')

for _ in range(5):
    print(d1.draw())
print()

print(CardDeck.RANKS)
print(d1.RANKS)

print(d1.get_ranks())
print(CardDeck.get_ranks())
print()

j1 = JokerDeck("Jerry")
print(j1)
j1.shuffle()
print(j1.cards)

print(len(d1), len(j1))
print(CardDeck.__len__(d1))

print(d1, j1)
print(str(d1), str(j1))

x = d1 + j1
print(x)

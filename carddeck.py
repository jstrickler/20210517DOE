"""
Card Deck

Provide a deck of cards that can be shuffled and dealt.
"""
import random

class CardDeck:  # (object)
    """
    One standard deck of 52 cards.

    Methods:
        shuffle()  -- shuffle the cards
        draw()     -- draw 1 card
    """
    RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()
    SUITS = 'Clubs Diamonds Hearts Spades'.split()

# self:Python::this:Java

    def __init__(self, dealer, jokers=False):
        self.dealer = dealer
        self._make_deck()

    def _make_deck(self):
        self._cards = []
        for suit in self.SUITS:
            for rank in self.RANKS:
                card = rank, suit  # tuple
                self._cards.append(card)

    @property
    def cards(self):
        return self._cards


    # instance method
    def shuffle(self):
        random.shuffle(self._cards)

    # instance method
    def draw(self):
        if len(self._cards) == 0:
            raise ValueError("No more cards")
        return self._cards.pop()

    # but properties are preferred...
    # # getter method
    # def get_dealer(self):
    #     return self._dealer

    # getter property
    @property   # decorator (REPLACER!)
    def dealer(self):
        return self._dealer

    # setter property
    @dealer.setter
    def dealer(self, dealer):
        if isinstance(dealer, str):
            self._dealer = dealer
        else:
            raise TypeError("Dealer must be a string")

    @property
    def dealer_upper(self):
        return self._dealer.upper()

    @property
    def spam(self):
        return self._spam

    @spam.setter
    def spam(self, value):
        # validate here if needed...
        self._spam = value

    @property
    def ham(self):
        return 42

    @property
    def toast(self):
        return self._toast

    @toast.setter
    def toast(self, value):
        pass

    @classmethod
    def get_ranks(cls):
        return cls.RANKS

    def __len__(self):
        return len(self._cards)

    def __str__(self):
        my_type = type(self)
        my_name = my_type.__name__
        return f"{my_name}({self.dealer}, {len(self)})"

    def __add__(self, other):
        my_type = type(self)
        tmp = my_type(self.dealer)
        tmp._cards = self.cards + other.cards
        return tmp


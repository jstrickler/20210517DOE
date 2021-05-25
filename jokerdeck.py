from carddeck import CardDeck

class JokerDeck(CardDeck):

    def _make_deck(self):
        super()._make_deck()
        for joker in "1", "2":
            card = joker, 'Joker'
            self._cards.append(card)

#        super().spam()  # search CardDeck and parents for method .spam()


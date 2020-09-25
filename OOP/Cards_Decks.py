from random import shuffle


class Card:

    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __repr__(self):
        return "{} of {}".format(self.value, self.suit)


class Deck:

    def __init__(self):
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        self.deal_cards = []
        self.cards = [Card(suit, value) for suit in suits for value in values]

    def shuffle_deck(self):
        shuffle(self.cards)
        return self

    def deal(self):
        if len(self.cards) == 0:
            raise IndexError("All cards have been dealt")
        self.deal_cards.append(self.cards.pop())
        return self.cards.pop()

    def put_in(self):
        if len(self.deal_cards) == 0:
            raise IndexError("Deck is full")
        self.cards.append(self.deal_cards.pop())


card = Card("Diamond", "A")
print(card)


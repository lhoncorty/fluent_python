import collections


# namedtuple 用于声明没有方法的类
Card = collections.namedtuple('Card', ['rank', 'suit'])


# 会用python原生的dunder method or magic methods. 运算符重载operator overloading.
# dunder 是液体残渣的意思
class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit)
                       for rank in self.suits
                       for suit in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]


beer_card = Card('7', 'spades')
print(beer_card)

deck = FrenchDeck()
print(len(deck))

print(deck[0])
print(deck[-1])

# Use random to randomly select a card:
from random import choice
print("Randomly select cards")
print(choice(deck))
print(choice(deck))
print(choice(deck))
print(choice(deck))

print("slicing")
print(deck[:3])
print(deck[12::13])



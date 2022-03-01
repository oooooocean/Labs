"""
Python最好的品质是一致性:
    - 标准接口.
    - 更加方便利用标准库.
"""

import collections
from random import choice
from math import hypot

Card = collections.namedtuple('Card', ['rank', 'suit'])
suit_values = {'♠': 3, '♣': 2, '♥': 1, '♦': 0}


class Poker:
    """
    扑克牌
    """
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = suit_values.keys()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                       for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, item):
        return self._cards[item]

    @classmethod
    def card_level(card):
        rank_value = Poker.ranks.index(card.rank)
        return rank_value * len(suit_values) + suit_values[card.suit]


class Vector:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    """
    repr()
    %格式化: %r 
    str.format: r!
    """
    def __repr__(self):
        return 'Vector(%r, %r)' % (self.x, self.y)

    """
    对用户友好
    str()/print() -> __str__ -> __repr__替代
    """
    def __str__(self):
        return '二维向量: %r, %r' % (self.x, self.y)

    def __abs__(self):
        return hypot(self.x, self.y)

    """
    解释器替代方案: __len__, 0 即 False
    """
    def __bool__(self):
        return bool(abs(self))
        # return bool(self.x or self.y)  # or 运算符可能会返回 x 或 y 本身的值

    """
    中缀运算符 +
    """
    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)


if __name__ == '__main__':
    poker = Poker()
    print('随机一张纸牌:', choice(poker))

    for card in sorted(poker, key=Poker.card_level):  # 隐式调用 iter(x) -> x.__iter__()
        print('排序:', card)

def poker(hands):
    hands = [Hand(cards) for cards in hands]
    return [hand.cards for hand in hands if hand == max(hands)]


class Hand:
    card_ranks = '23456789TJQKA'

    def __init__(self, cards):
        self.cards = cards
        self.ranks = sorted([r for r, c in cards], key=lambda x: Hand.rank(x))
        self.hand_rank = Hand.hand_rank(self)

    def __eq__(self, other):
        return self.ranks == other.ranks

    def __lt__(self, other):
        if self.hand_rank < other.hand_rank:
            return True

    @staticmethod
    def rank(item):
        return Hand.card_ranks.index(item)

    def hand_rank(self):
        groups = sorted([(self.ranks.count(r), r) for r in sorted(set(self.ranks), reverse=True, key=lambda x: Hand.rank(x))], reverse=True)
        counts, ranks = zip(*groups)
        flush = len(set([c for r, c in self.cards])) == 1
        straight = ''.join(self.ranks) in ''.join(Hand.card_ranks) or 'A' in self.ranks and ''.join(self.ranks[:-1]) in ''.join(Hand.card_ranks)
        return (8 if straight and flush else
                7 if counts == (4, 1) else
                6 if counts == (3, 2) else
                5 if flush else
                4 if straight else
                3 if counts == (3, 1, 1) else
                2 if counts == (2, 2, 1) else
                1 if counts == (2, 1, 1, 1) else
                0, ranks)

from collections import Counter
card_ranks = '23456789TJQKA'


def rank(item):
    return card_ranks.index(item)


def poker(hands):
    hands = [Hand(cards) for cards in hands]
    return [hand.cards for hand in hands if hand == max(hands)]


class Hand:
    def __init__(self, cards):
        self.cards = cards
        self.ranks = sorted([r for r, c in cards], key=lambda x: rank(x))
        self.colors = [c for r, c in cards]
        self.hand_rank = Hand.hand_rank(self)

    def __eq__(self, other):
        return self.ranks == other.ranks

    def __lt__(self, other):
        if self.hand_rank < other.hand_rank:
            return True
        if self.hand_rank > other.hand_rank:
            return False
        high_pair_choser = 0 if self.hand_rank == 2 else 1
        if self.hand_rank in [2, 6]:
            self_highpair, self_lowpair = sorted(Counter(self.ranks).most_common(2), key=lambda x: int(x[high_pair_choser]))[::-1]
            other_highpair, other_lowpair = sorted(Counter(other.ranks).most_common(2), key=lambda x: int(x[high_pair_choser]))[::-1]
            if rank(self_highpair[0]) < rank(other_highpair[0]):
                return True
            if rank(self_highpair[0]) > rank(other_highpair[0]):
                return False
            if rank(self_lowpair[0]) < rank(other_lowpair[0]):
                return True
            if rank(self_lowpair[0]) > rank(other_lowpair[0]):
                return False
        if self.hand_rank in [1, 3, 7]:
            self_pair_rank = Counter(self.ranks).most_common(1)[0][0]
            other_pair_rank = Counter(other.ranks).most_common(1)[0][0]
            if rank(self_pair_rank) < rank(other_pair_rank):
                return True
            if rank(self_pair_rank) > rank(other_pair_rank):
                return False
        for s, o in reversed(list(zip(self.ranks, other.ranks))):
            if rank(s) < rank(o):
                return True
        return False

    def hand_rank(self):
        groups = sorted([(self.ranks.count(rank), rank) for rank in sorted(set(self.ranks), reverse=True, key=lambda x: rank(x))], reverse=True)
        counts = [c for c, r in groups]
        flush = len(set(self.colors)) == 1
        straight = ''.join(self.ranks) in ''.join(card_ranks) or 'A' in self.ranks and ''.join(self.ranks[:-1]) in ''.join(card_ranks)
        if straight and flush:
            return 8
        if counts == [4, 1]:
            return 7
        if counts == [3, 2]:
            return 6
        if flush:
            return 5
        if straight:
            return 4
        if counts == [3, 1, 1]:
            return 3
        if counts == [2, 2, 1]:
            return 2
        if counts == [2, 1, 1, 1]:
            return 1
        return 0

from collections import Counter
hand_types = ['high_card', 'pair', '2pair', 'three_of_a_kind', 'straight', 'flush', 'full_house', 'four_of_a_kind', 'straight_flush']
card_ranks = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']


def rank(item):
    if item in hand_types:
        return hand_types.index(item)
    return card_ranks.index(item)


def poker(hands):
    hands = [Hand(cards) for cards in hands]
    return [hand.cards for hand in hands if hand == max(hands)]


class Hand:
    def __init__(self, cards):
        self.cards = cards
        self.ranks = sorted([r for r, c in cards], key=lambda x: rank(x))
        self.colors = [c for r, c in cards]
        self.hand_type = Hand.hand_type(self)

    def __eq__(self, other):
        return self.ranks == other.ranks

    def __lt__(self, other):
        if rank(self.hand_type) < rank(other.hand_type):
            return True
        if rank(self.hand_type) > rank(other.hand_type):
            return False
        high_pair_choser = 0 if self.hand_type == '2pair' else 1
        if self.hand_type in ['2pair', 'full_house']:
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
        if self.hand_type in ['pair', 'three_of_a_kind', 'four_of_a_kind']:
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

    @staticmethod
    def hand_type(hand):
        most_card_count = Counter(hand.ranks).most_common(1)[0][1]
        most_card_count_2nd = Counter(hand.ranks).most_common(2)[1][1]
        if len(set(hand.colors)) == 1 and ''.join(hand.ranks) in ''.join(card_ranks):
            return 'straight_flush'
        if most_card_count == 4:
            return 'four_of_a_kind'
        if most_card_count == 3 and most_card_count_2nd == 2:
            return 'full_house'
        if len(set(hand.colors)) == 1:
            return 'flush'
        if ''.join(hand.ranks) in ''.join(card_ranks) or 'A' in hand.ranks and ''.join(hand.ranks[:-1]) in ''.join(card_ranks):
            return 'straight'
        if most_card_count == 3:
            return 'three_of_a_kind'
        if most_card_count == 2 and most_card_count_2nd == 2:
            return '2pair'
        if most_card_count == 2:
            return 'pair'
        return 'high_card'

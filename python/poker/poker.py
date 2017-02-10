from collections import Counter
hand_types = ['high_card', 'pair', '2pair', 'pair3', 'straight', 'flush', 'full_house', 'pair4', 'straight_flush']
values_order = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']


def poker(hands):
    return [max([Hand(cards) for cards in hands]).lst]


def determine_hand_type(hand):
    most_nr = Counter(hand.values).most_common(1)[0][1]
    most_nr_2nd = Counter(hand.values).most_common(2)[1][1]
    if len(set(hand.colors)) == 1:
        if ''.join(hand.values) in ''.join(values_order):
            return hand_types.index('straight_flush')
        else:
            return hand_types.index('flush')
    if most_nr == 4:
        return hand_types.index('pair4')
    if most_nr == 3:
        if most_nr_2nd == 2:
            return hand_types.index('full_house')
        else:
            return hand_types.index('pair3')
    if ''.join(hand.values) in ''.join(values_order) or 'A' in hand.values and ''.join(hand.values[:-1]) in ''.join(values_order):
        return hand_types.index('straight')
    if most_nr == 2:
        if most_nr_2nd == 2:
            return hand_types.index('2pair')
        else:
            return hand_types.index('pair')
    return hand_types.index('high_card')


class Hand:
    def __init__(self, cards):
        self.lst = cards
        self.cards = [(value, color) for value, color in cards]
        self.values = sorted([value for value, color in self.cards], key=lambda x: values_order.index(x))
        self.colors = [color for value, color in self.cards]
        self.hand_type = determine_hand_type(self)

    def __lt__(self, other):
        if self.hand_type < other.hand_type:
            return True
        if self.hand_type > other.hand_type:
            return False
        if self.hand_type == hand_types.index('2pair'):
            self_highpair, self_lowpair = sorted(Counter(self.values).most_common(2), key=lambda x: int(x[0]))[::-1]
            other_highpair, other_lowpair = sorted(Counter(other.values).most_common(2), key=lambda x: int(x[0]))[::-1]
            if values_order.index(self_highpair[0]) < values_order.index(other_highpair[0]):
                return True
            if values_order.index(self_highpair[0]) > values_order.index(other_highpair[0]):
                return False
            if values_order.index(self_lowpair[0]) < values_order.index(other_lowpair[0]):
                return True
            elif values_order.index(self_lowpair[0]) > values_order.index(other_lowpair[0]):
                return False
        if self.hand_type == hand_types.index('full_house'):
            self_highpair, self_lowpair = sorted(Counter(self.values).most_common(2), key=lambda x: int(x[1]))[::-1]
            other_highpair, other_lowpair = sorted(Counter(other.values).most_common(2), key=lambda x: int(x[1]))[::-1]
            if values_order.index(self_highpair[0]) < values_order.index(other_highpair[0]):
                return True
            if values_order.index(self_highpair[0]) > values_order.index(other_highpair[0]):
                return False
            if values_order.index(self_lowpair[0]) < values_order.index(other_lowpair[0]):
                return True
            elif values_order.index(self_lowpair[0]) > values_order.index(other_lowpair[0]):
                return False
        if self.hand_type in [hand_types.index('pair'), hand_types.index('pair3'), hand_types.index('pair4')]:
            self_pair_value = Counter(self.values).most_common(1)[0][0]
            other_pair_value = Counter(other.values).most_common(1)[0][0]
            if values_order.index(self_pair_value) < values_order.index(other_pair_value):
                return True
            if values_order.index(self_pair_value) > values_order.index(other_pair_value):
                return False
        for s, o in reversed(list(zip(self.values, other.values))):
            if values_order.index(s) < values_order.index(o):
                return True
        return False

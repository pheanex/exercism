SUBLIST, SUPERLIST, EQUAL, UNEQUAL = 0, 1, 2, 3


def check_lists(a, b):
    a, b = [''.join(['{}'.format(c) for c in l]) for l in [a, b]]
    if a == b:
        return EQUAL
    elif a in b:
        return SUBLIST
    elif b in a:
        return SUPERLIST
    return UNEQUAL

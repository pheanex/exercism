def hexa(string):
    return sum(16**i * '0123456789ABCDEF'.index(c) for i, c in enumerate(reversed(string.upper())))

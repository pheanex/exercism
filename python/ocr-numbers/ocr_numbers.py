ocr_numbers = {'0': (' _ ', '| |', '|_|', '   '),
               '1': ('   ', '  |', '  |', '   '),
               '2': (' _ ', ' _|', '|_ ', '   '),
               '3': (' _ ', ' _|', ' _|', '   '),
               '4': ('   ', '|_|', '  |', '   '),
               '5': (' _ ', '|_ ', ' _|', '   '),
               '6': (' _ ', '|_ ', '|_|', '   '),
               '7': (' _ ', '  |', '  |', '   '),
               '8': (' _ ', '|_|', '|_|', '   '),
               '9': (' _ ', '|_|', ' _|', '   ')}


def number(l):
    return ''.join(digit(d) for d in zip(*[[r[i:i + 3] for i in range(0, len(r), 3)] for r in l]))


def digit(l):
    if len(l) != 4 or [i for i in l if len(i) != 3]:
        raise ValueError
    for k, v in ocr_numbers.items():
        if l == v:
            return k
    return '?'


def grid(digits):
    if any(i for i in digits if not i.isdigit()):
        raise ValueError
    return [''.join(i) for i in list(zip(*[list(ocr_numbers[n]) for n in digits]))]

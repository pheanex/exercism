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


def convert(lines):
    blocks = [lines[i:i+4] for i in range(0, len(lines), 4)]
    return ','.join(convert_block(block) for block in blocks)


def convert_block(block):
    return ''.join(convert_digit(d) for d in zip(*[[r[i:i + 3] for i in range(0, len(r), 3)] for r in block]))


def convert_digit(m):
    if len(m) != 4 or [i for i in m if len(i) != 3]:
        raise ValueError('Error')
    for key, value in ocr_numbers.items():
        if m == value:
            return key
    return '?'

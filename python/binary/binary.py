def parse_binary(string):
    if set(string) - set('01'):
        raise ValueError

    return sum([2**i for i, j in enumerate(string[::-1]) if j == '1'])

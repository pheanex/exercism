from itertools import zip_longest


def transpose(input_lines):
    lines = input_lines.splitlines()
    encoded = [line.replace(' ', '_') for line in lines]
    transposed = [''.join(line) for line in
                  zip_longest(*encoded, fillvalue=' ')]
    decoded = [line.rstrip().replace('_', ' ') for line in transposed]
    return '\n'.join(decoded)

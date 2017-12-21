from itertools import zip_longest


def transpose(input_lines):
    lines = input_lines.splitlines()
    encoded = [line.replace(' ', '_') for line in lines]
    encoded_transposed = [''.join(line) for line in zip_longest(*encoded, fillvalue=' ')]
    decoded_transposed = [line.rstrip().replace('_', ' ') for line in encoded_transposed]
    return '\n'.join(decoded_transposed)

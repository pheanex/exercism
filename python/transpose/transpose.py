from itertools import zip_longest


def transpose(input_lines):
    lines = input_lines.splitlines()
    encoded_lines = [line.replace(' ', '_') for line in lines]
    encoded_transposed_lines = [''.join(line) for line in zip_longest(*encoded_lines, fillvalue=' ')]
    decoded_tranposed_lines = [line.rstrip().replace('_', ' ') for line in encoded_transposed_lines]
    return '\n'.join(decoded_tranposed_lines)

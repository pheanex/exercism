from math import ceil
from itertools import zip_longest


def encode(message):
    message = ''.join(l.lower() for l in message if l.isalnum())
    if not message:
        return message
    column_length = ceil(len(message) ** 0.5)
    square = [message[i:i + column_length] for i in range(0, len(message), column_length)]
    chunks = [''.join(chunk) for chunk in zip_longest(*square, fillvalue=' ')]
    return ' '.join(chunks)

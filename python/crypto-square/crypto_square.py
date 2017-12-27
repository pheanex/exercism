from math import floor, sqrt, ceil


def encode(message):
    message = [l.lower() for l in message if l.isalnum()]
    chunks = []
    columns = floor(sqrt(len(message)))
    rows = ceil(len(message) / columns) if columns > 0 else 0
    for row in range(rows):
        chunks.append(''.join([letter for index, letter in enumerate(message) if index % rows == row]))
    return ' '.join(chunks)

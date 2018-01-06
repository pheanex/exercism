def valid_position(white, black):
    if any(x for x in white + black if not 0 <= x < 8) or white == black:
        raise ValueError('Invalid position')


def board(white, black):
    valid_position(white, black)
    return [''.join('_' if not (x, y) in [white, black] else 'W' if (x, y) == white else 'B' for y in range(0, 8)) for x in range(0, 8)]


def can_attack(white, black):
    valid_position(white, black)
    if white[0] == black[0] or white[1] == black[1] or abs(white[0] - black[0]) == abs(white[1] - black[1]):
        return True
    return False

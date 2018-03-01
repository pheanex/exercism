from itertools import cycle


def spiral(size):
    spiral_direction = cycle([(0, 1), (1, 0), (0, -1), (-1, 0)])
    matrix = [([0] * size) for _ in range(size)]
    row, column = 0, 0
    direction = next(spiral_direction)
    for number in range(1, size**2 + 1):
        matrix[row][column] = number
        if hit_border(matrix, row + direction[0], column + direction[1]):
            direction = next(spiral_direction)
        row += direction[0]
        column += direction[1]
    return matrix


def hit_border(matrix, row, column):
    try:
        return matrix[row][column] != 0
    except IndexError:
        return True

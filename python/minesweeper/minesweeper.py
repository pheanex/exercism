def board(matrix):
    def increment_block(x, y):
        for i in [i for i in range(x - 1, x + 2) if i >= 0]:
            for j in [j for j in range(y - 1, y + 2) if j >= 0]:
                if i < len(counter_matrix) and j < len(counter_matrix[i]):
                    counter_matrix[i][j] += 1

    if len(set(len(row) for row in matrix)) > 1:
        raise ValueError('Rows have different length')

    counter_matrix = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
    for row_index, row in enumerate(matrix):
        for column_index, char in enumerate(row):
            if char == '*':
                increment_block(row_index, column_index)
            if char not in [' ', '*']:
                raise ValueError('Invalid char')

    return [''.join([str(c) if d == ' ' and c != 0 else d for c, d in zip(a, b)]) for a, b in zip(counter_matrix, matrix)]

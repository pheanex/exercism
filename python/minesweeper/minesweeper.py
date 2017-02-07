def board(matrix):
    def column(lists, i):
        return [l[i] for l in lists]

    def increment_block(x, y):
        for i in range(x-1, x+2):
            for j in range(y-1, y+2):
                counter_matrix[i][j] += 1

    if not matrix[0][0] == matrix[0][-1] == matrix[-1][0] == matrix[-1][-1] == '+' or \
            set(matrix[0][1:-1] + matrix[-1][1:-1]) != set('-') or \
            set(column(matrix[1:-1], 0) + column(matrix[1:-1], -1)) != set('|') or \
            any(len(line) != len(matrix[0]) or set(line) - (set("+-|* ")) for line in matrix):
        raise ValueError

    counter_matrix = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
    for row_index, row in enumerate(matrix):
        for column_index, char in enumerate(row):
            if char == '*':
                increment_block(row_index, column_index)

    return [''.join([str(c) if d == ' ' and c != 0 else d for c, d in zip(a, b)]) for a, b in zip(counter_matrix, matrix)]

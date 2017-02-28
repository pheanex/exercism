def saddle_points(matrix):
    row_length = len(matrix[0]) if len(matrix) else 0
    for row in matrix:
        if row_length != len(row):
            raise ValueError

    points = set()
    for row in matrix:
        max_value_row = max(row)
        max_indices_row = [i for i, v in enumerate(row) if v == max_value_row]
        for row_index in max_indices_row:
            column = [row[row_index] for row in matrix]
            min_value_column = min(column)
            min_indices_column = [i for i, v in enumerate(column) if v == min_value_column]
            for column_index in min_indices_column:
                if max_value_row == min_value_column:
                    points.add((column_index, row_index))
    return points

def find_stop(row, column, word, puzzle):
    directions = [(0, 1), (0, -1), (1, 0), (1, 1), (1, -1), (-1, 0), (-1, 1), (-1, -1)]
    for d in directions:
        row_nr, column_nr = row, column
        for char_nr, char in enumerate(word):
            try:
                if puzzle[row_nr][column_nr] != char:
                    break
            except IndexError:
                break
            if char_nr == len(word) - 1:
                return row_nr, column_nr
            row_nr += d[0]
            column_nr += d[1]


def search(puzzle, word):
    for row_nr, row in enumerate(puzzle):
        for column_nr, char in enumerate(row):
            stop = find_stop(row_nr, column_nr, word, puzzle)
            if stop:
                return (row_nr, column_nr), stop

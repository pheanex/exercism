def count(lines=''):
    def valid_rectangle(x1, x2, y1, y2):
        if not lines[y1][x1] == lines[y2][x1] == lines[y1][x2] == lines[y2][x2] == '+' or \
                set(lines[y1][x1:x2] + lines[y2][x1:x2]) - set('+-') or \
                set([l[x1] for l in lines][y1:y2] + [l[x2] for l in lines][y1:y2]) - set('+|'):
            return False
        return True

    rectangles_count = 0
    for line_nr, line in enumerate(lines):
        row_crosses = [i for i, c in enumerate(line) if c == '+']
        line_pairs = [(i, j) for i in row_crosses for j in row_crosses if i < j]
        for a, b in line_pairs:
            a_column = [line[a] for line in lines[line_nr:]]
            column_crosses = [i + line_nr for i, c in enumerate(a_column) if c == '+']
            row_pairs = [(line_nr, i) for i in column_crosses if line_nr < i]
            for c, d in row_pairs:
                if valid_rectangle(a, b, c, d):
                    rectangles_count += 1
    return rectangles_count

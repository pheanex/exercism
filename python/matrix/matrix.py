class Matrix:
    def __init__(self, matrix_string):
        self.rows = [list(map(int, row.split())) for row in matrix_string.split("\n")]
        self.columns = [list(e) for e in list(zip(*self.rows))]

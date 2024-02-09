class Coordinate(dict):
    def __init__(self, row: int, column: int):
        self.column = column
        self.col = column
        self.row = row
        dict.__init__(self, column=column, row=row)

    def __str__(self):
        return '{"row": %s, "column": %s}' % (self.row, self.column)

    def __repr__(self) -> str:
        return str(self)

    def __eq__(self, other):
        return self.column == other.column and self.row == other.row

    def __lt__(self, other):
        _row = self.row

        def to_lexical(row):
            return chr(ord("A") + row)

        def to_str(coord):
            return to_lexical(coord.row) + str(coord.column)

        return to_str(self) < to_str(other)

    def __hash__(self):
        return hash((self.column, self.row))

    def is_adjacent(self, other, accept_diagonal=False):
        if self.column == other.column:
            return abs(self.row - other.row) == 1
        elif self.row == other.row:
            return abs(self.column - other.column) == 1
        elif abs(self.column - other.column) == 1 and accept_diagonal:
            return abs(self.row - other.row) == 1
        elif abs(self.row - other.row) == 0 and accept_diagonal:
            return abs(self.column - other.column) == 1
        return False

    def to_dict(self):
        return {"column": self.column, "row": self.row}

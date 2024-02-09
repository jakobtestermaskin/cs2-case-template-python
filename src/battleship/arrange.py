from typing import List
from utils import print
from coordinate import Coordinate
import random

from cell import CellState


def is_valid_position(
    grid: List[List[CellState]],
    positioned_boats: List[List[Coordinate]],
    boat_coordinates: List[Coordinate],
):
    for positioned_boat in positioned_boats:
        for point in positioned_boat:
            if point in boat_coordinates:
                return False

    def boat_has_only_one_column_or_row():
        columns = set([point.column for point in boat_coordinates])
        rows = set([point.row for point in boat_coordinates])

        return len(columns) == 1 or len(rows) == 1

    if not boat_has_only_one_column_or_row():
        return False

    row_size = len(grid)
    column_size = len(grid[0])

    for i, point in enumerate(boat_coordinates):
        if point.column >= column_size or point.row >= row_size:
            return False

        if i > 0:
            if not boat_coordinates[i - 1].is_adjacent(point):
                return False

    return True


def can_be_doward_going_veritical(row_size, entry, size):
    return (entry.row + size) <= row_size


def can_be_upward_going_veritical(entry, size):
    return (entry.row - size) >= -1


def can_be_rigth_going_horizontal(col_size, entry, size):
    return (entry.column + size) <= col_size


def can_be_left_going_horizontal(entry, size):
    return (entry.column - size) >= -1


def arrange_boats(grid: List[List[CellState]], boat_sizes: List[int]):
    """
    Place boats on the board.
    Input:
    -   grid: A two dimmentional grid where each cell is precent by a CellState.
        Example: [[CellState.UNKNOWN, CellState.MISS], [CellState.UNKNOWN, CellState.UNKNOWN]]  for a 2x2 grid.

        Here, grid[0][1] represents a miss in the first row and second column.

        Visualized:
        |---| M |
        |---|---|

     -  A list of integers. Each integer represents the length (size) of a boat.
        Example: [2, 2] (2 boats of size 2)

    Output: A list of lists of points. Each dictionary represents the position of a cell that makes a boat on the board.
    Example: [[Point(0, "A"), Point(1, "A")], [Point(0, "B"), Point(1, "B")]] (2 boats of size 2)
    """

    pass


if __name__ == "__main__":
    arrange_boats(
        [
            [
                CellState.UNKNOWN,
                CellState.UNKNOWN,
                CellState.UNKNOWN,
            ],
            [
                CellState.UNKNOWN,
                CellState.UNKNOWN,
                CellState.UNKNOWN,
            ],
            [
                CellState.UNKNOWN,
                CellState.UNKNOWN,
                CellState.UNKNOWN,
            ],
        ],
        [2, 2, 2],
    )

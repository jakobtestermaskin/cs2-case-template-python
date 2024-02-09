import os
import builtins

from typing import List
from cell import CellState
from coordinate import Coordinate


def is_docker():
    """Check if the code is running inside a docker container.

    Returns:
        bool: True if the code is running inside a docker container.
    """
    return os.path.isfile("/.dockerenv")


def print(*args, **kwargs):
    if is_docker():
        return builtins.print(*args, **kwargs, flush=True)
    else:
        return builtins.print(*args, **kwargs)


def flatmap(list_of_lists):
    return [item for list in list_of_lists for item in list]


def print_grid(grid: List[List[CellState]]):
    cell_space = 8
    amount_of_cells_per_row = len(grid[0])
    for row in grid:
        [
            print(
                f"%{cell_space}s|" % cell.value,
                end="",
            )
            for cell in row
        ]
        print(f"\n{'-'*(cell_space + 1) * amount_of_cells_per_row}\n")


def legal_moves(grid: List[List[CellState]]):
    _legal_moves = []
    for row in range(len(grid)):
        for column in range(len(grid[row])):
            if grid[row][column] == CellState.UNKNOWN:
                _legal_moves.append(Coordinate(row, column))

    return _legal_moves

from cell import CellState


def initial_grid(size):

    grid = []

    for i in range(size):
        grid.append([])
        for j in range(size):
            grid[i].append(CellState.UNKNOWN)

    return grid

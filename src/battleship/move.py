from coordinate import Coordinate
from utils import print, legal_moves

from typing import List


def shoot_coordinate(grid: List[List[str]]):  # enum to be created "miss|unknown|hit"
    return legal_moves(grid)


if __name__ == "__main__":
    shoot_coordinates = shoot_coordinate([["unknown"] * 10] * 10)

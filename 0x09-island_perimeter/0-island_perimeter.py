#!/usr/bin/python3
"""This module defines the function `island_perimeter`"""


def island_perimeter(grid):
    """Returns the perimeter of the island described in grid"""

    perimeter = 0
    row_size = len(grid)
    col_size = len(grid[0])

    for row in range(row_size):
        for col in range(col_size):
            if grid[row][col] == 1:
                if col - 1 < 0 or grid[row][col - 1] == 0:
                    perimeter += 1
                if col + 1 == col_size or grid[row][col + 1] == 0:
                    perimeter += 1
                if row - 1 < 0 or grid[row - 1][col] == 0:
                    perimeter += 1
                if row + 1 == row_size or grid[row + 1][col] == 0:
                    perimeter += 1
    return perimeter

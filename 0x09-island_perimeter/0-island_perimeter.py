#!/usr/bin/python3
"""This module defines the function `island_perimeter`"""


def island_perimeter(grid):
    """Returns the perimeter of the island described in grid"""
    count = 0
    row_no = -1
    dict = {}
    width = 0
    breadth = 0

    for row in grid:
        row_no += 1
        for i in row:
            if i == 1:
                count += 1
        dict[row_no] = count
        count = 0
    for k, v in dict.items():
        if v >= 1:
            width += 1
        if v > breadth:
            breadth = v
    perimeter = (2 * width) + (2 * breadth)
    return perimeter

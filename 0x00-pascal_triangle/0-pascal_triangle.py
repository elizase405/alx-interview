#!/usr/bin/python3
'''
def pascal_triangle(n):
    - Returns an empty list if n <= 0
    - You can assume n will be always an integer
'''


def pascal_triangle(n):
    ''' returns a list of lists of integers
        representing the Pascal’s triangle of n
    '''
    triangle = []

    if n <= 0:
        return triangle
    for i in range(n):
        row = []
        for j in range(i + 1):
            if (j == 0) or (j == i):
                row.append(1)
            else:
                row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
        triangle.append(row)

    return triangle

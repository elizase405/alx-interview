#!/bin/usr/python
'''
returns a list of lists of integers representing the Pascal’s triangle of n
def pascal_triangle(n):
    - Returns an empty list if n <= 0
    - You can assume n will be always an integer
'''

def pascal_triangle(n):
    lists = []
    if n <= 0:
        return lists
    for i in range(n):
        a_list = []
        a_list.append(1)

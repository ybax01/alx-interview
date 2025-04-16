#!/usr/bin/python3
"""
0-pascal_triangle
"""


def pascal_triangle(n):
    """
    Returns a list of lists of integers representing the Pascal’s triangle of n
    If n <= 0, it returns an empty list
    It assumes n is definetly an integer
    """
    pscl = []
    if n <= 0:
        return pscl
    pscl = [[1]]
    for i in range(1, n):
        temp = [1]
        for j in range(len(pscl[i-1]) - 1):
            temp.append(pscl[i-1][j]+pscl[i-1][j+1])
        temp.append(1)
        pscl.append(temp)
    return pscl

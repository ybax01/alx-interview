#!/usr/bin/python3
"""N Queens - Solving the classical problem"""
import sys


if len(sys.argv) != 2:
    print("Usage: nqueens N")
    exit(1)

if not isinstance(sys.argv[1], int):
    print("N must be a number")
    exit(1)

if sys.argv[1] < 4:
    print("N must be at least 4")
    exit(1)

n = int(sys.argv[1])

def queens_finder(n, i=0, cols=[], diagoA=[], diagoB=[]):
    """ find possible positions """
    if i < n:
        for j in range(n):
            if j not in cols and i + j not in diagoA and i - j not in diagoB:
                yield from queens_finder(n, i + 1, cols + [j], diagoA + [i + j], diagoB + [i - j])
    else:
        yield cols


def solve(n):
    """ solve """
    k = []
    i = 0
    for solution in queens_finder(n, 0):
        for s in solution:
            k.append([i, s])
            i += 1
        print(k)
        k = []
        i = 0


solve(n)
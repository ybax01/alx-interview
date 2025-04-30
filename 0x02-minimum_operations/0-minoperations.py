#!/usr/bin/python3
"""
Source code
"""


def minOperations(n):
    """
    Starting with a single 'H' in a file
    And the ability to Copy All and Paste
    Calculates the fewest number of operations needed
    to result in exactly n H characters in the file.
    """
    nOpe = 0
    minOpe = 2
    while n > 1:
        while n % minOpe == 0:
            nOpe += minOpe
            n //= minOpe
        minOpe += 1
    return nOpe

#!/usr/bin/python3
"""
Each box has keys to other boxes
Box 0 is always unlocked
A box is unlocked if a key with the same number is already found
"""


def canUnlockAll(boxes):
    """
    Determines if all the boxes can be opened.
    """
    n = len(boxes)
    checked_boxes = set([0])
    unchecked_boxes = set(boxes[0]).difference(set([0]))
    while len(unchecked_boxes) > 0:
        currentBox = unchecked_boxes.pop()
        if currentBox >= n or currentBox <= 0:
            continue
        if currentBox not in checked_boxes:
            unchecked_boxes = unchecked_boxes.union(boxes[currentBox])
            checked_boxes.add(currentBox)
    return n == len(checked_boxes)

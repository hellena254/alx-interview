#!/usr/bin/python3

"""
Module for canUnlockAll function
"""


def canUnlockAll(boxes):
    """
    Determines if all boxes can be opened.

    Parameters:
    boxes (list of list of int): List of lists where each sublist
    contains keys for other boxes

    Returns:
    bool: True if all boxes can be opened, False otherwise
    """
    n = len(boxes)
    unlocked = [False] * n
    unlocked[0] = True
    keys = [0]

    while keys:
        current_key = keys.pop()
        for key in boxes[current_key]:
            if key < n and not unlocked[key]:
                unlocked[key] = True
                keys.append(key)

    return all(unlocked)

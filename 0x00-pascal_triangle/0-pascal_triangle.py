#!/usr/bin/python3

"""
Module for pascal_triangle function
"""


def pascal_triangle(n):
    """
    Generates Pascal's triangle of size n

    Parameters:
    n (int): The size of the Pascal's triangle to generate

    Returns:
    list of list of int: Pascal's triangle represented as a list of lists
    """
    if n <= 0:
        return []

    triangle = [[1]]

    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(triangle[i-1][j-1] + triangle[i-1][j])
        row.append(1)
        triangle.append(row)

    return triangle

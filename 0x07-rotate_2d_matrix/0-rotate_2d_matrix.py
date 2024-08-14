#!/usr/bin/python3
"""
Function to rotate a 2D matrix by 90 degrees clockwise
"""


def rotate_2d_matrix(matrix):
    """
    Rotates an n x n 2D matrix by 90 degrees clockwise in place.
    Args:
        matrix (list of lists): The n x n matrix to be rotated.
    Returns:
        None. The matrix is modified in place.
    """

    n = len(matrix)

    # Transpose the matrix
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Reverse each row to get the final matrix
    for i in range(n):
        matrix[i].reverse()

#!/usr/bin/python3

def rotate_2d_matrix(matrix):
    """
    Rotate the matrix 90 degrees clockwise in a simpler way.
    """
    # Transpose the matrix
    n = len(matrix)
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Reverse each row
    for row in matrix:
        row.reverse()

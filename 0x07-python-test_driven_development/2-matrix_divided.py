#!/usr/bin/python3
"""Module for div matrix method

This 'Matrix_divided()' function used to divided
all element of matrix
"""


def matrix_divided(matrix, div):
    """matrix_divided is a function that divided
    all element of matrix

    Args:
        matrix: list of list of integer
        div: must be integer or float and can't be 0

    Raises:
        TypeError: if matrix or div not integer or float

    Return:
        return a new matrix with new value
    """
    if len(matrix) == 0:
        raise TypeError(
                'matrix must be a matrix (list of lists) of integers/floats')

    # Handle if matrix not int or float
    for row in matrix:
        # Handle if row not a list
        if type(row) not in [list] or len(row) == 0:
            raise TypeError(
                'matrix must be a matrix (list of lists) of integers/floats')
        # check if element is int and float or not
        for col in row:
            if type(col) not in [int, float]:
                raise TypeError(
                 'matrix must be a matrix (list of lists) of integers/floats')

    # Handle if the lists of matrix not the same size
    for row in matrix:
        if len(row) != len(matrix[0]):
            raise TypeError('Each row of the matrix must have the same size')

    # Handle division by 0 and element not int or float
    if div == 0:
        raise ZeroDivisionError('division by zero')
    if type(div) not in [int, float]:
        raise TypeError('div must be a number')

    new_matrix = [[round(col / div, 2) for col in row] for row in matrix]

    return new_matrix

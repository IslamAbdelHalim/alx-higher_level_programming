#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for row in matrix:
        new_row = []
        for col in row:
            new_row.append(col * col)
        new_matrix.append(new_row)
    return new_matrix

# List Comprehension way
# def square_matrix_simple(matrix=[]):
#    return [[col * col for col in row] for row in matrix]

#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not matrix:
        print()
    for row in matrix:
        for col in row:
            print(
                    "{:d} ".format(col) if col != row[len(row) - 1]
                    else "{:d}".format(col), end=""
                 )
        else:
            print()

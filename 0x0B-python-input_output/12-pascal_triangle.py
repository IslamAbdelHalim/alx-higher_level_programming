#!/usr/bin/python3
"""pascal triangle"""


def pascal_triangle(n):
    """function that make pascal tringle"""

    if n <= 0:
        return []
    pascal = []

    for row in range(n):
        current_row = []
        for col in range(row + 1):
            if col == 0 or col == row:
                current_row.append(1)
            else:
                current_row.append
                (pascal[row - 1][col - 1] + pascal[row - 1][col])
        pascal.append(current_row)
        return pascal

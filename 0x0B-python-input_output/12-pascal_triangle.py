#!/usr/bin/python3
"""pascal triangle"""


def pascal_triangle(n):
    """function that make pascal tringle"""

    if n <= 0:
        return []
    pascal = [[1]]

    while len(pascal) != n:
        pasc = pascal[-1]
        temp = [1]
        for i in range(len(pasc) - 1):
            temp.append(pasc[i] + pasc[i + 1])
        temp.append(1)
        pascal.append(temp)
    return pascal

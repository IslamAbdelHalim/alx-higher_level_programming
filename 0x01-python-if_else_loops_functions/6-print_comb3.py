#!/usr/bin/python3
for i in range(10):  # for first number
    for j in range(10):  # for Second number
        if i == j or i > j:
            continue
        else:
            if (i + j) != 17:
                print("{}{}, ".format(i, j), end="")
            else:
                print()

#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    sum = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            sum += 1
        except (TypeError, ValueError):
            continue
    print()
    return (sum)

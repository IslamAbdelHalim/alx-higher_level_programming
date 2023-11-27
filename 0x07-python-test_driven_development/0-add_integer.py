#!/usr/bin/python3
'''Module for add_integer method.

This method useed to add two integer and return the result

'''


def add_integer(a, b=98):
    """ add_integer is a function that add two interger

    Args:
        a: The first number
        b: The second number

    Raises:
        TypeError: if a or b are not int or float

    Return:
        The return value the sum two numbers
    """
    if type(a) not in [int, float]:
        raise TypeError('a must be an integer')
    elif type(b) not in [int, float]:
        raise TypeError('b must be an integer')
    return int(a) + int(b)

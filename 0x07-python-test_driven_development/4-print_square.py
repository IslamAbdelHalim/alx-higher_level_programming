#!/usr/bin/python3
'''Module for print a square with '''

def print_square(size):
    """ print_square is a function that print a square

    Args:
        size: The size of square
    
    Raises:
        TypeError: if size not integer
        TypeError: if size is a float or less than 0
        ValueError: if size is less than 0
    
    Return:
        nothing just print the square
    """
    if type(size) is not int:
        raise TypeError('size must be an integer')
    if size < 0:
        raise ValueError('size must be >= 0')
    if type(size) is float and size < 0:
        raise TypeError('size must be an integer')
    
    for x in range(size):
        for y in range(size):
            print('#', end="")
        print()

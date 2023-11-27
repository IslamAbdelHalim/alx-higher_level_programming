#!/usr/bin/python2
"""1-square is a module"""
Square = __import__('0-square').Square

class Square:
    """size are the size of square

    The __init__ method is used to initialize the class
    """
    def __init__(self, size):
        self.__size = size

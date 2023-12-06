#!/usr/bin/python3
"""Square Modure"""

# check the size


def check_size(size):
    """function that check the size attribute"""
    if type(size) is not int:
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")


class Square:
    """Square class"""

    def __init__(self, size=0):
        """initialize the variable

        Args:
            size: The size of square
        Raises:
            TypeError: if the size is not integer
            ValueError: if the size is less than 0
        """
        check_size(size)

        self.size = size

    @property
    def size(self):
        """function to get attribute"""
        return self.__size

    @size.setter
    def size(self, size):
        """function to set attributs"""
        check_size(size)

        self.__size = size

    def area(self):
        """function calc the area

        Retuen:
            The current square area
        """
        return self.__size ** 2

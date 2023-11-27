#!/usr/bin/python3
"""Square Modure"""


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
        self.__size = size

    def area(self):
        """function calc the area

        Retuen:
            The current square area
        """
        return self.__size ** 2

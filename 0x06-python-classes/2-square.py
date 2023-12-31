#!/usr/bin/python3
"""Square Module"""


class Square:
    """Square class"""

    def __init__(self, size=0):
        """initialize the variavble

        Args:
            size: The size of square

        Raises:
            TypeError: If size is not an integer
            ValueError: If size is less than 0
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

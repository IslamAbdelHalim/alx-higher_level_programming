#!/usr/bin/python3
"""Rectangle Module"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Square is a sub class of Rectangle
    """
    def __init__(self, size):
        """
        initialization the variables

        Args:
            self: The instance of object
            size: The size of square
        """
        self.integer_validator("size", size)
        self.__size = size
        Rectangle.__init__(self, self.__size, self.__size)
    def __str__(self):
        """
        return The string of class
        """
        return f"[Square] {self.__size}/{self.__size}"

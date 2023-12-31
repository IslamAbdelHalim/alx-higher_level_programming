#!/usr/bin/python3
"""Square Class"""


class Square:
    """Define a square class"""
    def __init__(self, size=0):
        """Initialization property"""
        self.size = size

    @property
    def size(self):
        """Getter size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter Size"""
        if type(value) is not float and type(value) is not int:
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Methos that Calc the area"""
        return self.__size ** 2

    def __eq__(self, other):
        """Method check if 2 squares are equals"""
        return self.area() == other.area()

    def __ne__(self, other):
        """Method check if 2 squares not equals"""
        return self.area() != other.area()

    def __gt__(self, other):
        """Method check if self is greater than other"""
        return self.area() > other.area()

    def __lt__(self, other):
        """Method check if self is less than other"""
        return self.area() < other.area()

    def __ge__(self, other):
        """Method check if self greater than or equal other"""
        return self.area() >= other.area()

    def __le__(self, other):
        """Method check if self less than or equal other"""
        return self.area() <= other.area()

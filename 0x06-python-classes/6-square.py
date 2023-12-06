#!/usr/bin/python3
"""Square Module"""


def check_size(size):
    """function to check the size"""
    if type(size) is not int:
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")


class Square:
    """ Square Class"""
    def __init__(self, size=0, position=(0, 0)):
        """
        Initialize varialbles

        Args:
            self: the instance of object
            size: The size of square
            position: the position of square
        """
        self.position = position
        check_size(size)
        self.size = size

    @property
    def size(self):
        """get size"""
        return self.__size

    @size.setter
    def size(self, value):
        """set size"""
        check_size(value)
        self.__size = value

    @property
    def position(self):
        """get position"""
        return self.__position

    @position.setter
    def position(self, value):
        """set position"""
        if type(value) is not tuple or len(value) != 2 \
                or not all(isinstance(x, int) and x >= 0 for x in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """function return the area"""
        return self.__size ** 2

    def my_print(self):
        if self.__size == 0:
            print()
        else:
            for x in range(self.__position[1]):
                print()
            for col in range(self.__size):
                for sp in range(self.__position[0]):
                    print(' ', end="")
                print("#" * (self.__size))

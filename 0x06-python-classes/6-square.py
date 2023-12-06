#!/usr/bin/python3
"""Square Modure"""

# check the size


def check_size(size):
    """function that check the size attribute"""
    if type(size) is not int:
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")


def check_position(position):
    """function that check if the position is tuple and int"""
    if type(position) is not tuple or type(position[0]) is not int or\
            type(position[1]) is not int or len(position) != 2:
        raise TypeError("position must be a tuple of 2 positive integers")


class Square:
    """Square class"""

    def __init__(self, size=0, position=(0, 0)):
        """initialize the variable

        Args:
            size: The size of square
        Raises:
            TypeError: if the size is not integer
            ValueError: if the size is less than 0
        """
        check_size(size)
        self.size = size
        check_position(position)
        self.position = position

    @property
    def size(self):
        """function to get attribute"""
        return self.__size

    @size.setter
    def size(self, size):
        """function to set attributs"""
        check_size(size)
        self.__size = size

    @property
    def position(self):
        """function get position attr"""
        return self.__position

    @position.setter
    def position(self, value):
        """function that set a position value"""
        check_position(value)
        self.__position = value

    def area(self):
        """function calc the area

        Retuen:
            The current square area
        """
        return self.__size ** 2

    def my_print(self):
        """function that print the square"""
        if self.__size == 0:
            print("")
        else:
            for i in range(self.__position[1]):
                print()
            for col in range(self.__size):
                for space in range(self.__position[0]):
                    print(" ", end="")
                for row in range(self.__size):
                    print("#", end="")
                print("")

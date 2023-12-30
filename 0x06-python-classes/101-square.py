#!/usr/bin/python3
"""Square Class"""


class Square:
    """Class of square"""
    def __init__(self, size=0, position=(0, 0)):
        """initialization of square attributes"""
        self.size = size
        self.position = position

    @property
    def size(self):
        """Getter size"""
        return self.__size

    @size.setter
    def size(self, value):
        """setter size"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Getter Position"""
        return self.__position

    @position.setter
    def position(self, value):
        """Setter position"""
        if type(value) is not tuple or len(value) != 2 \
                or not all(isinstance(x, int) and x >= 0 for x in value):
            raise TypeError("position must be a tuple of 2 positive integer")
        self.__position = value

    def area(self):
        """Method that calculate the area"""
        return self.__size ** 2

    def my_print(self):
        """Method that print the square shape"""
        if self.size == 0:
            print()
        for y in range(self.__position[1]):
            print()
        for row in range(self.__size):
            for x in range(self.__position[0]):
                print(" ", end="")
            print("#" * self.__size)

    def __str__(self):
        """Magic Method"""
        form = ""
        if self.size == 0:
            form += "\n"
        for y in range(self.__position[1]):
            form += "\n"
        for row in range(self.__size):
            for x in range(self.__position[0]):
                form += ' '
            form += "#" * self.__size
            form += "\n"
        return form.rstrip()

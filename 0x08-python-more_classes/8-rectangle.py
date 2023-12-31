#!/usr/bin/python3
"""Rectangle Module"""


class Rectangle:
    """
    Rectangel class
    """

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """initialize the data attribute"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """getter the private witdth"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter the new value"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """getter the private height"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter the new value of height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """method to calc area"""
        return self.__width * self.__height

    def perimeter(self):
        """method calc perimeter"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width + self.height) * 2

    def __str__(self):
        """to return on string"""
        shape = ""
        if self.__width != 0 and self.__height != 0:
            shape = "\n".join(str(self.print_symbol) * self.__width
                              for i in range(self.__height))
        return shape

    def __repr__(self):
        """return a string representation of the rectangle"""
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    # function that delete the instance or (object)
    def __del__(self):
        """Function that delete the object and print a messege"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() > rect_2.area():
            return rect_1
        elif rect_1.area() < rect_2.area():
            return rect_2
        else:
            return rect_1

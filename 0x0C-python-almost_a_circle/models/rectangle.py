#!/usr/bin/python3
"""Rectangle module"""

from models.base import Base


class Rectangle(Base):
    """Rectangle Class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        initialize the variables

        Args:
            self - instance object
            width - width attribute
            height - height attribute
            x - argument
            y - argument
            id - argument
        """
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.width = width

        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.height = height

        if type(x) is not int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.x = x

        if type(y) is not int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.y = y

        super().__init__(id)

    # width attribute
    @property
    def width(self):
        """ width getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """width setter"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    # height attribute
    @property
    def height(self):
        """getter height"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    # x attribute
    @property
    def x(self):
        """getter x"""
        return self.__x

    @x.setter
    def x(self, value):
        """setter x"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    # y attribute
    @property
    def y(self):
        """getter y"""
        return self.__y

    @y.setter
    def y(self, value):
        """setter y"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    # Area Method
    def area(self):
        """ function that return the area of rectangle"""
        return self.__width * self.__height

    # Display Method
    def display(self):
        """function that display"""
        # y axis
        for y in range(self.__y):
            print()
        for h in range(self.__height):
            # x axis
            for x in range(self.__x):
                print(' ', end="")
            for w in range(self.__width):
                print('#', end='')
            print()

    # use __str__
    def __str__(self):
        """function that return the string"""
        return f"[Rectangle] \
({self.id}) {self.__x}/{self.__y} - {self.__width}/{self.__height}"

    # Update Method
    def update(self, *args, **kwargs):
        """
        function that update and assign
        an argument to each attribute
        """
        if len(args) != 0:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.__width = args[1]
            if len(args) >= 3:
                self.__height = args[2]
            if len(args) >= 4:
                self.__x = args[3]
            if len(args) >= 5:
                self.__y = args[4]
        else:
            for kay, value in kwargs.items():
                setattr(self, kay, value)

    def to_dictionary(self):
        """
        function that returns the dictionary
        representation of a Rectangle
        """
        rect_dict = {
                "id": self.id,
                "width": self.width,
                "height": self.height,
                "x": self.x,
                "y": self.y,
                }
        return rect_dict

#!/usr/bin/python3
'''Rectangle Class

A Rectangle Class

'''


class Rectangle:
    '''Rectangle with size'''

    def __init__(self, width=0, height=0):
        '''__init__

        The __init__ method initializes the width and\
             height methods of the Rectangle.

        Attributes:
            width (:obj:'int', optional): The width of the Rectangle
            height (:obj:'int', optional): The height of the Rectangle

        Raises:
            TypeError: If 'width' or  'height' is not an integer

            ValueError: if 'width' or  'height' < 0
        '''

        if type(width) is not int:
            raise TypeError("size must be an integer")
        if width < 0:
            raise ValueError("size must be >= 0")
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")

        self.__width = width
        self.__height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value

    def area(self):
        '''Returns the current rectangle area'''
        return self.__width * self.__height

    def perimeter(self):
        '''Returns the current rectangle perimeter'''
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return (2 * self.__width) + (2 * self.__height)

    def __print_rectangle(self):
        '''
        Prints the rectangle with the character '#'

        Return:
        An empty string if height or width is 0
        '''

        if self.__width == 0 or self.__height == 0:
            print()
        else:
            i, j = 1, 1
            for i in range(self.__height + 1):
                side = ''
                for j in range(self.__width + 1):
                    side += '#'
                    j += 1
                side += '\n'
                i += 1
            return side

        def str(self):
            '''Prints the rectangle'''
            return self.__print_rectangle()

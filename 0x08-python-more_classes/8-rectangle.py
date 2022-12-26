#!/usr/bin/python3
'''Rectangle Class

A Rectangle Class

'''


class Rectangle:
    '''Rectangle with size'''

    number_of_instances = 0
    print_symbol = '#'

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
        Rectangle.number_of_instances += 1

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

    def __str__(self):
        '''
        Prints the rectangle with the character '#'

        Return:
        The string of the rectangle
        '''
        rectangle = ''
        if self.__width == 0 or self.__height == 0:
            return rectangle
        else:
            for i in range(self.__height):
                rectangle += (str(self.print_symbol) * self.__width) + '\n'
        return rectangle[:-1]

    def __repr__(self):
        '''Returns the representation of the Rectangle'''
        w = str(eval('self.__width'))
        h = str(eval('self.__height'))

        return 'Rectangle(' + w + ', ' + h + ')'

    def __del__(self):
        '''
        Prints a message when an instance of Rectangle is deleted

        '''

        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if isinstance(rect_1, Rectangle) and isinstance(rect_2, Rectangle):
            if (rect_1.area > rect_2.area):
                return rect_1
            elif (rect_1.area == rect_2.area):
                return rect_1
            else:
                return rect_2
        elif isinstance(rect_1, Rectangle) is False:
            raise TypeError('rect_1 must be an instance of Rectangle')
        elif isinstance(rect_2, Rectangle) is False:
            raise TypeError('rect_2 must be an instance of Rectangle')
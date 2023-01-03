#!/usr/bin/python3
'''Base Geometry class'''


class BaseGeometry:
    '''Base Geometry class'''
    def area(self):
        '''Area exception'''
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        '''Validates value'''
        self.name = str(name)
        if type(value) is not int:
            raise TypeError(f'{name} must be an integer')
        if value <= 0:
            raise ValueError(f'{name} must be greater than 0')

'''Rectangle Class'''


class Rectangle(BaseGeometry):
    '''Rectangle class with wodth and height'''
    def __init__(self, width, height):
        '''init method with height and width as integers'''
        self.__width = width
        self.__height = height
        self.__width.integer_validator()
        self.__height.integer_validator()

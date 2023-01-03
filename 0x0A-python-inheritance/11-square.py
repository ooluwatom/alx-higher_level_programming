#!/usr/bin/python3
'''Rectangle module'''

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    '''Square class'''
    def __init__(self, size):
        self.integer_validator('size', size)
        self.__size = size

    def area(self):
        '''Area of the square'''
        return self.__size * self.__size

    def __str__(self):
        return '[Square] ' + str(self.__width) + '/' + str(self.__height)

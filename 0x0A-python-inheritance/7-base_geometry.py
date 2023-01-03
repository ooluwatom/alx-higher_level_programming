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

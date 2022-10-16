#!/usr/bin/python3
'''Square Class

A Square Class

'''


class Square:
    '''Square with size'''

    def __init__(self, size=0):
        '''__init__

        The __init__ method initializes the size method of the square.

        Attributes:
            size (:obj:'int', optional): The size of the square

        Raises:
            TypeError: If 'size' type is not an integer

            ValueError: if 'size' < 0
        '''

        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    def area(self):
        '''area(self)

        The area function returns the current square area

        Returns:
            Area of current square
        '''

        self.area = self.size ** 2
        return self.area

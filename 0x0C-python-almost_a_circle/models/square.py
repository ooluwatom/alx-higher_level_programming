#!/usr/bin/python3
'''Import rectangle class'''
from models.rectangle import Rectangle


class Square(Rectangle):
    '''Square Class'''
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return f'[Square] ({self.id}) {self.__x}/{self.__y} - \
            {self.__height}/{self.__width}'

    @property
    def size(self):
        return self.size

    @size.setter
    def size(self, value):
        self.__height = value
        self.__width = value
#!/usr/bin/python3
'''Base Class

    This is the base class for the entire operation'''


class Base:
    '''Base class'''
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            self.__nb_objects += 1
            self.id = self.__nb_objects

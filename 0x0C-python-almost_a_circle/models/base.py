#!/usr/bin/python3
'''Base Class

    This is the base class for the entire operation'''


class Base:
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            __nb_objects += 1
            self.id = __nb_objects
 
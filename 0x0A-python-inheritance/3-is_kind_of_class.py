#!/usr/bin/python3
'''Function that checks whether object is an instance of a class\
    or instance of a class that inherited from the class'''


def is_kind_of_class(obj, a_class):
    '''Function that checks whether object is an instance of a class\
    or instance of a class that inherited from the class'''
    return isinstance(obj, a_class)

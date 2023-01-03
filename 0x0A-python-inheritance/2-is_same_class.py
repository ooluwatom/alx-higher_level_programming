#!/usr/bin/python3
'''This function returns whether an object is an instance of\
    the specified class or not'''


def is_same_class(obj, a_class):
    '''Returns true if the object is an instance of the specified class'''
    if type(obj) == a_class:
        return True
    return False

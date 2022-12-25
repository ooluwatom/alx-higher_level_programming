#!/usr/bin/python3
def add_integer(a, b=98):
    '''
    This function adds two integers
    Return - a + b
    '''
    if type(a) != float or type(a) != int:
        raise TypeError('a must be an integer')
    elif type(b) != float or type(b) != int:
        raise TypeError('b must be an integer')
    if type(a) == float:
        a = int(a)
    if type(b) == float:
        b = int(b)
    return a + b

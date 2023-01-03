#!/usr/bin/python3
'''Function that checks whether object is an instance of a class\
    or instance of a class that inherited from the class'''


def is_kind_of_class(obj, a_class):
    if issubclass(obj, a_class) or isinstance(obj, a_class):
        return True
    return False

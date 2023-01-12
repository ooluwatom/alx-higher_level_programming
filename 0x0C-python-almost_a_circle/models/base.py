#!/usr/bin/python3
'''Base Class

    This is the base class for the entire operation'''


import json


class Base:
    '''Base class'''
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        '''Returns json representation sof list_dictionaries'''
        if list_dictionaries is None:
            return "[]"
        else:
            return json.JSONEncoder().encode(list_dictionaries)

    def save_to_file(cls, list_objs):
        '''Write Json string representation of list_objs to a file'''
        filename = f'{cls.__name__}.json'
        list_dic = []
        if list_objs is None:
            pass
        else:
            for i in range(len(list_objs)):
                list_dic.append(list_objs[i].to_dictionary())

        lists = cls.to_json_string(list_dic)

        with open(filename, 'w') as f:
            f.write(lists)

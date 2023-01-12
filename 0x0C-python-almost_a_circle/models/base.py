#!/usr/bin/python3
'''Base Class

    This is the base class for the entire operation'''


import json
from os import path


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

    @classmethod
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

    @staticmethod
    def from_json_string(json_string):
        '''Returns the list of the json string representation'''
        les = []
        if json_string is None or len(json_string) < 1:
            return les
        else:
            return json.JSONDecoder().decode(json_string)

    @classmethod
    def create(cls, **dictionary):
        '''Returns an instance with all attributes already set'''
        if cls.__name__ == 'Square':
            dummy = cls(3)

        if cls.__name__ == 'Rectangle':
            dummy = cls(3, 4)

        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        '''Returns a list of instances'''
        filename = f'{cls.__name__}.json'
        les = []
        if path.exists(filename) is False:
            return les

        with open(filename, mode='r', encoding='utf-8') as f:
            objs = cls.from_json_string(f.read())
            instances = []

            for elem in objs:
                instances.append(cls.create(**elem))

            return instances

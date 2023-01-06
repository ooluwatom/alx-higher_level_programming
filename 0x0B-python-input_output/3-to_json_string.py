#!/usr/bin/python3
'''json module'''


import json
'''This function returns the JSON representation of a string'''


def to_json_string(my_obj):
    '''Return a JSON representation of string'''
    return json.JSONEncoder().encode(my_obj)

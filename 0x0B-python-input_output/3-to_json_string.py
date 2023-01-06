#!/usr/bin/python3
import json
'''This function returns thte JSON representation of a string'''


def to_json_string(my_obj):
    '''Return a JSON representation of string'''
    return json.JSONEncoder().encode(my_obj)

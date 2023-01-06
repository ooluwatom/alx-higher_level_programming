#!/usr/bin/python3
'''json module'''


import json
'''This function returns the object representation of a JSON string'''


def from_json_string(my_str):
    '''Return an object representation of a JSON string'''
    return json.JSONDecoder().decode(my_str)

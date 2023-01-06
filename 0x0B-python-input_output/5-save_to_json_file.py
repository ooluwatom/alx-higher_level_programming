#!/usr/bin/python3
'''json module'''


import json
'''This function writes an object to text file using its JSON representation'''


def save_to_json_file(my_obj, filename):
    '''Write object to text file using JSON representation'''
    with open(filename, 'w') as f:
        json.dump(my_obj, f)

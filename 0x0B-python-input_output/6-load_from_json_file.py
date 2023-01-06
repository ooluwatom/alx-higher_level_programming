#!/usr/bin/python3
'''json module'''


import json
'''This function loads an object from a json file'''


def load_from_json_file(filename):
    '''Loads object from a json file'''
    with open(filename) as f:
        json.load(f)
        for i in f:
            print(i)

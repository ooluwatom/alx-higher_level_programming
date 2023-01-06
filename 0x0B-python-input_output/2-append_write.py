#!/usr/bin/python3
'''This function appends a string and returns the number\
     of characters written'''


def append_write(filename="", text=""):
    '''Appends a string and returns number of characters written'''
    with open(filename, mode='a', encoding="UTF-8") as f:
        f.write(text)
    return len(text)

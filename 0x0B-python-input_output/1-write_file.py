#!/usr/bin/python3
'''This function writes a text file and returns the number of characters written'''


def write_file(filename="", text=""):
    '''Writes a text file and returns number of characters written'''
    with open(filename, mode='w', encoding="UTF-8") as f:
        f.write(text)
    return len(text)

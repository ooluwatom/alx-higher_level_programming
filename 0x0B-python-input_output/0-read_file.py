#!/usr/bin/python3
'''This function reads a text file and prints it out'''


def read_file(filename=""):
    '''Reads a text file and prints it'''
    with open(filename, mode='r', encoding="UTF-8") as f:
        for line in f:
            print(line, end='')

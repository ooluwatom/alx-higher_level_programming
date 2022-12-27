#!/usr/bin/python3
'''Function that prints a text with 2 new lines after \
    each of these characters: ., ? and :'''


def text_indentation(text):
    '''Function to add lines'''
    if type(text) is not str:
        raise TypeError('text must be a string')
    for letter in text:
        if letter == '.' or letter == '?' or letter == ':':
            text.replace(text[letter + 1], '\n\n')

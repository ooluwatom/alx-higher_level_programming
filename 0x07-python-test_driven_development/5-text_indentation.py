#!/usr/bin/python3
'''Function that prints a text with 2 new lines after \
    each of these characters: ., ? and :'''


def text_indentation(text):
    '''Function to add lines'''
    if type(text) is not str:
        raise TypeError('text must be a string')
    for letter in text:
        if letter == '.' or letter == '?' or letter == ':':
            print(letter, end='\n\n')
        else:
            print(letter, end='')
    print(text)

text_indentation('Tomi.boy')
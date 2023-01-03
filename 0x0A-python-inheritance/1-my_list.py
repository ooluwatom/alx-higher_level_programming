#!/usr/bin/python3
'''This class inherits from the List class'''


class MyList(list):
    '''List class'''
    def print_sorted(self):
        '''This method prints the list in a sorted manner'''
        return sorted(self)

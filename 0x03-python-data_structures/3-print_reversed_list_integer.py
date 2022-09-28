#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    my_list.reverse()
    if len(my_list) != None:
        for element in my_list:
            print('{:d}'.format(element))

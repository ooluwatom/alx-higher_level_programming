#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        print(my_list[x], end='')
        x += 1
    except IndexError:
        return x + 1

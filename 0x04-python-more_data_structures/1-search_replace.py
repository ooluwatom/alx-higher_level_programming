#!/usr/bin/python3
def search_replace(my_list, search, replace):
    i = 0
    for i in range(len(my_list)):
        if my_list[i] == search:
            my_list[i] == replace
            i += 1
        else:
            continue
    return my_list

#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list =[]
    i = 0
    for i in range(len(my_list)):
        if my_list[i] == search:
            new_list.append(replace)
            i += 1
        else:
            new_list.append(search)
    return my_list

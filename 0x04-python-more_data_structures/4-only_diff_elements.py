#!/usr/bin/python3
def common_elements(set_1, set_2):
    list_1 = [i for i in set_1 if i in set_2]
    list_2 = [j for j in set_2 if j in set_1]
    return [list_1, list_2]

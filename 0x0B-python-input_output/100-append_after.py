#!/usr/bin/python3
'''This functions inserts a line of text \
    after each  line containing a specific string'''


def append_after(filename="", search_string="", new_string=""):
    '''This function inserts a line of text \
        after each  line containing a specific string'''
    text = ""
    with open(filename) as r:
        for line in r:
            text += line
            if search_string in line:
                text += new_string
    with open(filename, "w") as w:
        w.write(text)

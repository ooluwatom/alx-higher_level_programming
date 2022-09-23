#!/usr/bin/python3
def remove_char_at(str, n):
    new_str = ""
    for character in str:
        if character == str[n]:
            continue
        else:
            new_str += character
    return new_str

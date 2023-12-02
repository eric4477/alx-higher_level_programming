#!/usr/bin/python3:
def no_c(my_string):
    chars_list = list(my_string)
    for char in chars_list:
        if char == 'c' or char == 'C':
            chars_list.remove(char)
    return("".join(chars_list))

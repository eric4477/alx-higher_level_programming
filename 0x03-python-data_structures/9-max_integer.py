#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    else:
        greatest_num = 0
        for num in my_list:
            if num > greatest_num:
                greatest_num = num
    return greatest_num

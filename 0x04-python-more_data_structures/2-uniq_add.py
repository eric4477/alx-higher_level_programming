#!/usr/bin/python3
def uniq_add(my_list=[]):
    total = 0
    new_list = set([num for num in my_list])
    for unq_num in new_list:
        total += unq_num
    return total

#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    my_list_1 = my_list[:]
    if idx >= 0 and idx < len(my_list_1):
        my_list_1[idx] = element
    return my_list_1

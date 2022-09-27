#!/usr/bin/python3

def new_in_list(my_list, idx, element):

    draft = len(my_list)

    if idx < 0 or idx >= draft:
        return my_list
    my_list[idx] = element
    return my_list

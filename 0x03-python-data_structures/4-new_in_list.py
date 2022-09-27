#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    new_cpy = my_list[:]
    draft = len(new_cpy)

    if idx < 0 or idx >= draft:
        return new_cpy

    new_cpy[idx] = element
    return new_cpy

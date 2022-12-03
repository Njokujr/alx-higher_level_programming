#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    '''
    Replaces an element in a list at a specific position
    Without modifying the original list.
    '''
    new_list = my_list[:]
    if idx < 0:
        return new_list

    elif idx >= len(my_list):
        return new_list

    else:
        new_list[idx] = element
        return new_list

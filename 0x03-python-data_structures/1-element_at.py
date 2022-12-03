#!/usr/bin/python3
def element_at(my_list, idx):
    '''
    Gets an element in a list at given index
    And returns it
    '''
    if idx < 0:
        return None

    elif idx >= len(my_list):
        return None

    else: 
        return my_list[idx]

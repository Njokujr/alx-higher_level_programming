    '''
    Gets an element in a list at given index
    And returns it
    '''
#!/usr/bin/python3
def element_at(my_list, idx):
    if idx >= len(my_list) or idx < 0:
        return

    return (my_list[idx])

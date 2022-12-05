#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    div2_list = []
    for n in my_list:
        if n % 2 == 0:
            div2_list.append(True)
        else:
            div2_list.append(False)
     return div2_list

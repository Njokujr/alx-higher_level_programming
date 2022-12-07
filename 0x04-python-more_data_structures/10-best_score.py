#!/usr/bin/python3
def best_score(a_dictionary):
    max_num = 0
    best = None
    if type(a_dictionary) is dict:
        for key, value in a_dictionary.items():
            if value > max_num:
                max_num = value
                best = key
    return best

#!/usr/bin/python3
"""
Defines a JSON file-writing function.
"""
import json


def save_to_json_file(my_obj, filename):
    with open(filename, "w") as f:
        """ write an object to a text file using JSON representation."""
        json.dump(my_obj, f)

#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Defines a JSON file-writing function.
& write an object to a text file using JSON representation.
"""
import json


def save_to_json_file(my_obj, filename):
    with open(filename, "w") as f:
        json.dump(my_obj, f)

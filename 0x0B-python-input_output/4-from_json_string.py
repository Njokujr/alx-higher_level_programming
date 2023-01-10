#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Defines a JSON-to-object function.
& Return the python object representation of a JSON string.
"""
import json


def from_json_string(my_str):
    return json.loads(my_str)

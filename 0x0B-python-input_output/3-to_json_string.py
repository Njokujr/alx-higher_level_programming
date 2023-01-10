#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Defines a string-to-JSON function.
& Return the JSON representation of a string object.
"""
import json


def to_json_string(my_obj):
    return json.dumps(my_obj)

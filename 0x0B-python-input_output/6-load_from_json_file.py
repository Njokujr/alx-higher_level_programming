#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Defines a JSON file-reading function.
& Creates a Python object from a JSON file.
"""
import json


def load_from_json_file(filename):
    with open(filename) as f:
        return json.load(f)

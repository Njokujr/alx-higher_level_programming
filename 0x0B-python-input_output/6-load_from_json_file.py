#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Defines a JSON file-reading function.
"""
import json


def load_from_json_file(filename):
    with open(filename) as f:
        """ Creates a Python object from a JSON file."""
        return json.load(f)

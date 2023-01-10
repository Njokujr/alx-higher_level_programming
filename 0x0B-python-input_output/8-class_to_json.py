#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Defines a python class-to-JSON function.
& Returns the dictionary representation of a simple data structure.
"""


def class_to_json(obj):
    return obj.__dict__

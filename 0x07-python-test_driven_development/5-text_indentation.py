#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Author: Victory Njoku
"""


def text_indentation(text):
    """
    prints a string with 2 new lines after '.', '?', and ':'
    Args:
        text (int): text to print
    Raises:
        TypeError: "text must be a string"
    """
    if type(text) is not str:
        raise TypeError("text must be a string")
    tmp = text.replace(".", ".\n\n")
    tmp = tmp.replace(":", ":\n\n")
    tmp = tmp.replace("?", "?\n\n")
    p = tmp.splitlines(True)
    ls_strip = []
    for k in p:
        if k == "\n":
            ls_strip.append("\n")
        else:
            ls_strip.append(k.lstrip())
    print("".join(ls_strip), end="")

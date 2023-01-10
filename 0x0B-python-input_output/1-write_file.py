#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Defines a file-writing function.
& returns the number of characters written
"""


def write_file(filename="", text=""):
    """Write a string to a UTF8 text file.

    Args:
        filename (str): The name of the file to write.
        text (str): The text to write to the file.

    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)

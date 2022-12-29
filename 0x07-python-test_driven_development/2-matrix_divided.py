#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Author: Victory Njoku
"""

def matrix_divided(matrix, div):
    """
    divides all elements of a matrix
    Args:
        matrix (list of list): list of list of int or float
        div (int/float): integer or float to divide for
    Raises:
        TypeError: Exception if elements in matrix and div are not integer or
            float; Each row in the matrix have the same size
        ZeroDivisionError: Exception if div is 0
    Return:
        The result to divide matrix by div
    """
    if len(matrix):
        n = len(matrix[0])
        for row in matrix:
            if n != len(row):
                raise TypeError(
                        "Each row of the matrix must have the same size")
            for i in row:
                if type(i) not in [int, float]:
                    raise TypeError("matrix must be a matrix\
                            (list of lists) of integers/floats")
    new_matrix = [[round(i/div, 2) for i in row] for row in matrix]
    return new_matrix

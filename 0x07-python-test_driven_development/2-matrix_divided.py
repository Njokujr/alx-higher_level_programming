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
    newList = []
    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    for i in matrix:
        k = []
        if type(i) is not list:
            raise TypeError("matrix must be a matrix\
 (list of lists) of integers/floats")
        if(len(matrix[0]) != len(i)):
            raise TypeError("Each row of the matrix\
 must have the same size")
        for j in range(len(i)):
            if (type(i[j]) is not int) and (type(i[j]) is not float):
                raise TypeError("matrix must be a matrix\
(list of lists) of integers/floats")
            k.append(round(((i[j]) / div), 2))
        newList.append(k)
    return newList

#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
Author: Victory Njoku
'''


class Rectangle:
    '''
    Defines a rectangle figure
    '''

    def __init__(self, width=0, height=0):
        '''
        Initialise method for Rectangle
        Attr:
            width-> The width of the rectangle
            height-> (int, optional): The height of the rectangle
        '''
        self.__height = height
        self.__width = width

    def __str__(self):
        '''
        str method to print rectangle

        Returns the string with # rectangle
        '''
        string = ""
        if self.__width == 0 or self.__height == 0:
            return string

        for i in range(self.__height):
            for j in range(self.__width):
                string += '#'
            if i < self.__height - 1:
                string += '\n'
        return string

    def __repr__(self):
        '''
        Returns repr method for object rectangle

        Returns string (str)
        '''
        return "Rectangle(" + str(self.__width) + ", " + str(self.__height) +\
            ")"

    def __del__(self):
        '''
        delete method for rectangle
        '''
        print("Bye rectangle...")

    @property
    def height(self):
        '''
        Returns the height of the rectangle
        '''
        return self.__height

    @height.setter
    def height(self, value):
        '''
        Attr:
            height-> The height of the rectangle

        Raises:
            TypeError: If height is not an integer
            ValueError: If height is less than 0
        '''
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    @property
    def width(self):
        '''
        Returns the width of the rectangle
        '''
        return self.__width

    @width.setter
    def width(self, value):
        '''
        Attr:
            width-> The width of the rectangle
        Raises:
            TypeError: If width is not an integer
            ValueError: If width is less than 0
        '''
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    def area(self):
        '''
        Calculate the area of the rectangle

        Returns the area of the rectangle
        '''
        return self.__width * self.__height

    def perimeter(self):
        '''
        Calculates the perimeter of the rectangle

        Returns the perimeter of the rectangle
        '''
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

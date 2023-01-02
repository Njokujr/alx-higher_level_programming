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
            width-> the width of the Rectangle
            height-> the height of the Rectangle

        '''
        self.__height = height
        self.__width = width

    def __str__(self):
        '''
        str method to print Rectangle

        Returns the string with # Rectangle
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
         returns the repr method for object Rectangle

         Returns string '''
        return "Rectangle(" + str(self.__width) + ", " + str(self.__height) +\
               ")"

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
            height-> the height of the rectangle

         Raises:
            TypeError: If the height is not an integer
            ValueError: If height is less than 0 '''

        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    @property
    def width(self):
        '''
         Returns the width of the Rectangle
         '''
        return self.__width

    @width.setter
    def width(self, value):
        '''
         Attr:
            width-> the width of the Rectangle

         Raises:
            TypeError: If width is not an integer
            ValueError: If the width is less than 0
         '''
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    def area(self):
        '''
         Calculates the area of the Rectangle
         Returns the area of the Rectangle
         '''
        return self.__width * self.__height

    def perimeter(self):
        '''
         Calculates the perimeter of the Rectangle


         Returns the perimeter of the Rectangle
         '''
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

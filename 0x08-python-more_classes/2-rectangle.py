#!/usr/bin/python3
# _*_ coding: utf-8 _*_
'''
Author:Victory Njoku
'''


class Rectangle:
    '''
    Defines a rectangle figure
    '''

    def __init__(self, width=0, height=0):
        '''
        Initialise method for Rectangle

        Attr:
            width-> The width of the Rectangle
            height-> The height of the Rectangle
        self.width = width
        self.height = height
        '''
        self.__width = width
        self.__height = height

    @property
    def height(self):
        '''
        Returns the height of the Rectangle
        '''
        return self.__height

    @height.setter
    def height(self, value):
        '''
        Attr:
            height-> The height of the Rectangle

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
        Returns the width of the Rectangle
        '''
        return self.__width

    @width.setter
    def width(self, value):
        '''
        Attr:
            width-> The width of the Rectangle


        Raises:
            TypeError: If width is not an integer
            ValueError: if width is less than 0
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

         Returns:
            The area of the Rectangle
          '''
        return self.__width * self.__height

    def perimeter(self):
        '''
        Calculates the perimeter of the Rectangle

        Returns:
            The perimeter of the rectangle
        '''
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

# 0x04. Python - More Data Structures: Set, Dictionary.

# Requirements.
General
Allowed editors: vi, vim, emacs
All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
All your files should end with a new line
The first line of all your files should be exactly #!/usr/bin/python3
A README.md file, at the root of the folder of the project, is mandatory
Your code should use the pycodestyle (version 2.8.)
All your files must be executable
The length of your files will be tested using wc

# Mandatory_tasks.
0. Squared simple
	A function that computes the square value of all integers of a matrix.

1. Search and replace
	A function that replaces all occurrences of an element by another in a new list.

2. Unique addition
	A function that adds all unique integers in a list (only once for each integer).

3. Present in both
	A function that returns a set of common elements in two sets.

4. Only differents
	A function that returns a set of all elements present in only one set.

5. Number of keys
	A function that returns the number of keys in a dictionary.

6. Print sorted dictionary
	A function that prints a dictionary by ordered keys.

7. Update dictionary
	A function that replaces or adds key/value in a dictionary.

8. Simple delete by key
	A function that deletes a key in a dictionary.

9. Multiply by 2
	A function that returns a new dictionary with all values multiplied by 2

10. Best score
	A function that returns a key with the biggest integer value.

11. Multiply by using map
	A function that returns a list with all values multiplied by a number without using 
	any loops.

12. Roman to Integer
	A function def roman_to_int(roman_string): that converts a Roman numeral to an integer.

# Advanced_tasks.
13. Weighted average!
	a function that returns the weighted average of all integers tuple (<score>, <weight>).

14. Squared by using map
	a function that computes the square value of all integers of a matrix using map.

15. Delete by value
	a function that deletes keys with a specific value in a dictionary..

16. CPython #1: PyBytesObject
	Create two C functions that print some basic info about Python lists and Python bytes 		objects.
	"""Python lists:

#**Prototype: void print_python_list(PyObject *p);
Format: see example
Python bytes:

#**Prototype: void print_python_bytes(PyObject *p);
Format: see example
Line “first X bytes”: print a maximum of 10 bytes
If p is not a valid PyBytesObject, print an error message (see example)
Read /usr/include/python3.4/bytesobject.h
About:

#**Python version: 3.4
Your shared library will be compiled with this command line: gcc -Wall -Werror -Wextra -pedantic -std=c99 -shared -Wl,-soname,libPython.so -o libPython.so -fPIC -I/usr/include/python3.4 103-python.c
You are not allowed to use the following macros/functions:
Py_SIZE
Py_TYPE
PyList_GetItem
PyBytes_AS_STRING
PyBytes_GET_SIZE"""

# 0x0A. PYTHON _ INHERITANCE

# PYTHON TEST CASES
Allowed editors: vi, vim, emacs
All your files should end with a new line
All your test files should be inside a folder tests
All your test files should be text files (extension: .txt)
All your tests should be executed by using this command: python3 -m doctest ./tests/*
All your modules should have a documentation (python3 -c 'print(__import__("my_module").__doc__)')
All your classes should have a documentation (python3 -c 'print(__import__("my_module").MyClass.__doc__)')
All your functions (inside and outside a class) should have a documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)' and python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)')
A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)
We strongly encourage you to work together on test cases, so that you don’t miss any edge case

# DOCUMENTATION
Do not use the words import or from inside your comments, the checker will think you try to import some modules


# MANDATORY_TASKS
0. Lookup
	a function that returns the list of available attributes and methods of an object

1. My list
	a class MyList that inherits from list

2. Exact same object
	a function that returns True if the object is exactly an instance of the specified class ; otherwise False

3. Same class or inherit from
	a function that returns True if the object is an instance of, or if the object is an instance of a class that inherited from, the specified class ; otherwise False

4. Only sub class of
	a function that returns True if the object is an instance of a class that inherited (directly or indirectly) from the specified class ; otherwise False

5. Geometry module
	Write an empty class BaseGeometry

6. Improve Geometry
	a class BaseGeometry (based on 5-base_geometry.py)

7. Integer validator
	Write a class BaseGeometry (based on 6-base_geometry.py).

8. Rectangle
	Write a class Rectangle that inherits from BaseGeometry (7-base_geometry.py).

9. Full rectangle
	Write a class Rectangle that inherits from BaseGeometry (7-base_geometry.py). (task based on 8-rectangle.py)

10. Square #1
	Write a class Square that inherits from Rectangle (9-rectangle.py)

11. Square #2
	Write a class Square that inherits from Rectangle (9-rectangle.py). (task based on 10-square.py)



# ADVANCED_TASKS
12. My integer
	Write a class MyInt that inherits from int

13. Can I?
	Write a function that adds a new attribute to an object if it’s possible

# 0x0B. PYTHON - INPUT/OUTPUT

# PYTHON TEST CASE
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


# MANDATORY_TASKS
0. Read file
	Write a function that reads a text file (UTF8) and prints it to stdout

1. Write to a file
	Write a function that writes a string to a text file (UTF8) and returns the number of characters written.

2. Append to a file
	Write a function that appends a string at the end of a text file (UTF8) and returns the number of characters added

3. To JSON string
	Write a function that returns the JSON representation of an object (string)

4. From JSON string to Object
	Write a function that returns an object (Python data structure) represented by a JSON string

5. Save Object to a file
	Write a function that writes an Object to a text file, using a JSON representation

6. Create object from a JSON file
	Write a function that creates an Object from a “JSON file”

7. Load, add, save
	Write a script that adds all arguments to a Python list, and then save them to a file

8. Class to JSON
	Write a function that returns the dictionary description with simple data structure (list, dictionary, string, integer and boolean) for JSON serialization of an object.

9. Student to JSON
	Write a class Student that defines a student by:
		Public instance attributes:
			first_name
			last_name
			age

10. Student to JSON with filter
	Write a class Student that defines a student by: (based on 9-student.py)

11. Student to disk and reload
	Write a class Student that defines a student by: (based on 10-student.py)

12. Pascal's Triangle
	Technical interview preparation:

You are not allowed to google anything
Whiteboard first
Create a function def pascal_triangle(n): that returns a list of lists of integers representing the Pascal’s triangle of n:

Returns an empty list if n <= 0
You can assume n will be always an integer
You are not allowed to import any module



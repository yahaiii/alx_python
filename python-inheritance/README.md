# Python Inheritance Tasks
This repository contains the solutions for the Python Inheritance tasks for the ALX iSWE program. Each task is provided in a separate file with its accompanying test case file, and the directory structure is organized as follows:


```
python-inheritance/
│
├── 0-is_same_class.py
├── 0-main.py
├── 1-is_kind_of_class.py
├── 1-main.py
├── 2-inherits_from.py
├── 2-main.py
├── 3-base_geometry.py
├── 3-main.py
├── 4-base_geometry.py
├── 4-main.py
├── 5-base_geometry.py
├── 5-main.py
├── 6-rectangle.py
├── 6-main.py
├── 7-rectangle.py
├── 7-main.py
├── 8-square.py
├── 8-main.py
├── README.md
```
## Task Descriptions
### 0. Exact same object
Write a function that returns True if the object is exactly an instance of the specified class ; otherwise False.

* Prototype: def is_same_class(obj, a_class):
* You are not allowed to import any module.

### 1. Same class or inherit from
Write a function that returns True if the object is an instance of, or if the object is an instance of a class that inherited from, the specified class ; otherwise False.

* Prototype: def is_kind_of_class(obj, a_class):
* You are not allowed to import any module

### 2. Only sub class of
Write a function that returns True if the object is an instance of a class that inherited (directly or indirectly) from the specified class ; otherwise False.

* Prototype: def inherits_from(obj, a_class):
* You are not allowed to import any module

### 3. Geometry module
Write an empty class BaseGeometry.

* You are not allowed to import any module

### 4. Improve Geometry
Write a class BaseGeometry (based on 3-base_geometry.py).

* Public instance method: def area(self): that raises an Exception with the message area() is not implemented
* You are not allowed to import any module

### 5. Integer validator
Write a class BaseGeometry (based on 4-base_geometry.py).

* Public instance method: def area(self): that raises an Exception with the message area() is not implemented
* Public instance method: def integer_validator(self, name, value): that validates value:
    * you can assume name is always a string
    * if value is not an integer: raise a TypeError exception, with the message <name> must be an integer
    * if value is less or equal to 0: raise a ValueError exception with the message <name> must be greater than 0
* You are not allowed to import any module

### 6. Rectangle
Write a class Rectangle that inherits from BaseGeometry (5-base_geometry.py).

* Instantiation with width and height: def __init__(self, width, height):
    * width and height must be private. No getter or setter
    * width and height must be positive integers, validated by integer_validator

### 7. Full rectangle
Write a class `Rectangle` that inherits from `BaseGeometry (5-base_geometry.py)`. (task based on `6-rectangle.py`)

* Instantiation with width and height: def __init__(self, width, height)::
    * width and height must be private. No getter or setter
    * width and height must be positive integers validated by integer_validator
* the area() method must be implemented
* print() should print, and str() should return, the following rectangle description: `[Rectangle] <width>/<height>`

### 8. Square #1
Write a class Square that inherits from Rectangle (7-rectangle.py):

* Instantiation with size: def __init__(self, size)::
    * size must be private. No getter or setter
    * size must be a positive integer, validated by integer_validator
* the area() method must be implemented


## How to Use
To run any specific task, simply execute the corresponding Python file. For example, to run `0-is_same_class.py`, use the following command:

`python3 0-is_same_class.py`

Make sure you have Python installed on your system.

Happy coding!
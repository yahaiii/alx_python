"""
This module contains the Square class.

The Square class represents a square with a specified size. It has a private instance attribute __size, which stores the size of the square.

Attributes:
    __size (int): The size of the square.

Methods:
    __init__(self, size=0): Initialize a Square object with an optional size.
    area(self): Calculate and return the area of the square.

Raises:
    TypeError: If size is not an integer.
    ValueError: If size is less than 0.
"""


class Square:
    def __init__(self, size=0):
        """
        Initialize a Square object.

        Args:
            size (int): Optional size of the square. Default is 0.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        
        self.__size = size

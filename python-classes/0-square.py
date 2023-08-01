"""
My Square Class

This module defines a simple Square class to represent squares in a two-dimensional space.
The Square class has an attribute 'size' to store the size of the square. The size is a positive
integer that represents the length of each side of the square.

Attributes:
    size (int): The size of the square, i.e., the length of each side.

Methods:
    __init__(self, size): Constructor method to initialize the Square object with a given size.

Example:
    # >>> square1 = Square(5)

Note:
    This implementation of the Square class does not perform type or value validation on the 'size' attribute.
    It is assumed that the 'size' attribute will always be a positive integer.
"""

class Square:
    """
    A class that represents a square.

    Attributes:
        __size (int): The size of the square.
    
    Methods:
        __init__(self, size): Initializes a Square object with the given size.
    """

    def __init__(self, size):
        """
        Initializes a Square object with the given size.

        Args:
            size (int): The size of the square.
        """
        self.__size = size
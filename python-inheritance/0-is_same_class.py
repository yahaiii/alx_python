"""
is_same_class.py

This module defines a function that checks if an object is exactly an instance of a specified class.

Functions:
    is_same_class(obj, a_class): Check if the object is an instance of the specified class.

Examples:
        # >>> is_same_class(5, int)
        True
        # >>> is_same_class("hello", str)
        True
        # >>> is_same_class([], list)
        True
        # >>> is_same_class(5, float)
        False
"""

def is_same_class(obj, a_class):
    """
    Check if the object is exactly an instance of the specified class.

    Args:
        obj (Any): The object to be checked.
        a_class (type): The class to check against.

    Returns:
        bool: True if the object is an instance of the specified class; otherwise, False.
    """
    return type(obj) is a_class
    """
    Returns:
        bool: True if the object is an instance of the specified class; otherwise, False.
    """

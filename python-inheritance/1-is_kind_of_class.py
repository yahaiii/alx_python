"""
Module: 1-is_kind_of_class

This module defines a function that checks if an object is an instance of a given class or a subclass.

Functions:
    is_kind_of_class(obj, a_class): Check if the object is an instance of, or if the object is an instance
    of a class that inherited from, the specified class.

Example:
    is_kind_of_class(5, int)  # Output: True
    is_kind_of_class("hello", str)  # Output: True
    is_kind_of_class([], list)  # Output: True
    is_kind_of_class(5, float)  # Output: False
"""
def is_kind_of_class(obj, a_class):
    """
    Check if the object is an instance of, or if the object is an instance of a class
    that inherited from, the specified class.

    Args:
        obj (Any): The object to be checked.
        a_class (type): The class to check against.

    Returns:
        bool: True if the object is an instance of the specified class or a subclass;
              otherwise, False.
    """
    return isinstance(obj, a_class)
    """
    Returns:
        bool: True if the object is an instance of the specified class; otherwise, False.
    """
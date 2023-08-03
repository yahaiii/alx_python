"""
Module: 3-base_geometry

This module defines an empty base class for other geometry-related classes.

Classes:
    BaseGeometry: A base class for other geometry-related classes.
"""


class BaseGeometry:
    """
    This class serves as the base for other geometry-related classes.
    """
    pass

def __dir__(self):
        """
        Returns:
            list: List of attributes excluding __init_subclass__.
        """
        # Get the list of attributes of the class (excluding __init_subclass__)
        attributes = [attr for attr in dir(type(self)) if attr != '__init_subclass__']

        # Return the new list of attributes
        return attributes

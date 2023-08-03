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

def dir(self):
        """
        Returns:
            list: List of attributes excluding __init_subclass__.
        """
        # Get the list of attributes of the class (excluding __init_subclass__)
        attributes = super().__dir__()
        # Remove __init_subclass__ from the list of attributes.
        new_attributes = [attribute for attribute in attributes if attribute != "__init_subclass__"]
        return new_attributes

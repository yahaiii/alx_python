"""
Module: 3-base_geometry

This module defines an empty base class for other geometry-related classes.

Classes:
    BaseGeometry: A base class for other geometry-related classes.
"""

class definitionOverrideMetaClass(type):
      def __dir__(cls):
        """
        Returns:
            list: List of attributes excluding __init_subclass__.
        """
        return [attribute for attribute in super().__dir__() if attribute != '__init_subclass__']


class BaseGeometry(metaclass=definitionOverrideMetaClass):
    """
    This class serves as the base for other geometry-related classes.
    """
    pass

